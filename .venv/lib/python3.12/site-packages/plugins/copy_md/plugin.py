import os
import shutil
from pathlib import Path

from mkdocs.utils import log
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin

class CopyMDPlugin(BasePlugin):
    config_scheme = (
        ("source_dir", Type(str, required=True)),
        ("target_dir", Type(str, required=True)),
    )

    def on_post_build(self, config):
        source = self.config["source_dir"]
        target_rel = self.config["target_dir"]
        site_dir = config["site_dir"]
        
        # Validate and resolve the source path
        try:
            source_path = Path(source).resolve()
            if not source_path.exists():
                log.warning(f"Source directory '{source}' not found; skipping copy-md operation.")
                return
            if not source_path.is_dir():
                log.error(f"Source path '{source}' is not a directory; skipping copy-md operation.")
                return
        except (OSError, ValueError) as e:
            log.error(f"Invalid source_dir '{source}': {e}")
            return
        
        # Validate and resolve the target path to prevent path traversal attacks
        try:
            # Resolve the target path relative to site_dir
            target = os.path.join(site_dir, target_rel)
            target_path = Path(target).resolve()
            site_dir_path = Path(site_dir).resolve()
            
            # Ensure the target is within the site directory bounds using pathlib
            try:
                target_path.relative_to(site_dir_path)
            except ValueError:
                log.error(f"Security violation: target_dir '{target_rel}' resolves to path outside site directory")
                log.error(f"Resolved target: {target_path}")
                log.error(f"Site directory: {site_dir_path}")
                return
                
        except (OSError, ValueError) as e:
            log.error(f"Invalid target_dir '{target_rel}': {e}")
            return

        # Remove existing target if present to avoid stale files
        if target_path.exists():
            shutil.rmtree(target_path)
            log.debug(f"Removed existing target directory: {target_path}")

        try:
            shutil.copytree(source_path, target_path)
            log.info(f"Successfully copied raw Markdown from '{source_path}' to '{target_path}'")
        except Exception as e:
            log.error(f"Failed to copy Markdown files from '{source_path}' to '{target_path}': {e}")
