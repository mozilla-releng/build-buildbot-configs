SLAVES = {
    "linux": ["debsign1", "debsign2"],
}

BRANCHES = {
    "mozilla-central": {},
    "mozilla-1.9.2": {},
}
BRANCHES["mozilla-central"]["script_repo_tag"] = "default"
BRANCHES["mozilla-central"]["nightly_config_file"] = "deb_repos/staging_trunk_nightly.json"
BRANCHES["mozilla-central"]["nightly_platforms"] = ["chinook", "fremantle", "fremantle-qt"]
BRANCHES["mozilla-central"]["enable_release"] = False

BRANCHES["mozilla-1.9.2"]["script_repo_tag"] = "default"
BRANCHES["mozilla-1.9.2"]["nightly_config_file"] = "deb_repos/staging_1.1_nightly.json"
BRANCHES["mozilla-1.9.2"]["nightly_platforms"] = ["chinook", "fremantle"]
BRANCHES["mozilla-1.9.2"]["enable_release"] = True
BRANCHES["mozilla-1.9.2"]["release_config_file"] = "deb_repos/staging_1.1_release.json"
BRANCHES["mozilla-1.9.2"]["release_platforms"] = ["chinook", "fremantle"]
