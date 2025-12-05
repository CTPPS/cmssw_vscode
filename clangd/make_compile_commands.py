from pathlib import Path
import json
import os

if not all([item in os.environ for item in ["CMSSW_BASE", "CMSSW_RELEASE_BASE"]]):
    raise Exception("Run cmsenv first")

CMSSW_BASE = Path(os.environ["CMSSW_BASE"])
CMSSW_RELEASE_BASE = Path(os.environ["CMSSW_RELEASE_BASE"])

# Load the local/release compilation commands
with (CMSSW_BASE / "compile_commands.json").open("r") as f:
    compile_commands_preFix = json.load(f)
with (CMSSW_RELEASE_BASE / "compile_commands.json").open("r") as f:
    compile_commands_release = json.load(f)
    files_release_map = {
        item["file"]: idx for idx, item in enumerate(compile_commands_release)
    }

# Update the compile commands of the release with the local area changes
for entry in compile_commands_preFix:
    file = entry["file"]
    if file in files_release_map:
        pos = files_release_map[file]
        compile_commands_release[pos]["directory"] = entry["directory"]
        compile_commands_release[pos]["command"] = entry["command"]
    else:
        compile_commands_release.append(
            {
                "command": entry["command"],
                "file": entry["file"],
                "directory": entry["directory"],
            }
        )

# Store the new commands into the compile_commands.json
with (CMSSW_BASE / "compile_commands.json").open("w") as f:
    json.dump(compile_commands_release, f, indent=4)
