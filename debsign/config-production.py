SLAVES = {
    "linux": ["debsign1"],
}

BRANCHES = {
    "mozilla-central": {},
    "mozilla-2.1": {},
}
BRANCHES["mozilla-central"]["script_repo_tag"] = 'default'
BRANCHES["mozilla-central"]["nightly_config_file"] = "deb_repos/trunk_nightly.json"
BRANCHES["mozilla-central"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-central"]["enable_release"] = False
BRANCHES["mozilla-central"]["nightly_hour"] = 4

BRANCHES["mozilla-2.1"]["script_repo_tag"] = 'default'
BRANCHES["mozilla-2.1"]["nightly_config_file"] = "deb_repos/mozilla-2.1_nightly.json"
BRANCHES["mozilla-2.1"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-2.1"]["enable_release"] = True
BRANCHES["mozilla-2.1"]["release_config_file"] = "deb_repos/4.0_release.json"
BRANCHES["mozilla-2.1"]["release_platforms"] = ["fremantle"]
BRANCHES["mozilla-2.1"]["nightly_hour"] = 4