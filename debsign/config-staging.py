SLAVES = {
    "linux": ["debsign1", "debsign2"],
}

BRANCHES = {
    "mozilla-central": {},
}
BRANCHES["mozilla-central"]["script_repo_tag"] = "default"
BRANCHES["mozilla-central"]["nightly_config_file"] = "deb_repos/staging_trunk_nightly.json"
BRANCHES["mozilla-central"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-central"]["enable_release"] = True
BRANCHES["mozilla-central"]["release_config_file"] = "deb_repos/staging_4.0_release.json"
BRANCHES["mozilla-central"]["release_platforms"] = ["fremantle"]
BRANCHES["mozilla-central"]["nightly_hour"] = 9
