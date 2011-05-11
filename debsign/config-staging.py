SLAVES = {
    "linux": ["debsign1", "debsign2"],
}

BRANCHES = {
    "mozilla-central": {},
    "mozilla-2.1": {},
    "mozilla-mobile-5.0": {},
}
BRANCHES["mozilla-central"]["script_repo_tag"] = "default"
BRANCHES["mozilla-central"]["nightly_config_file"] = "deb_repos/staging_trunk_nightly.json"
BRANCHES["mozilla-central"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-central"]["enable_release"] = False
BRANCHES["mozilla-central"]["nightly_hour"] = 9

BRANCHES["mozilla-2.1"]["script_repo_tag"] = "default"
BRANCHES["mozilla-2.1"]["nightly_config_file"] = "deb_repos/staging_mozilla-2.1_nightly.json"
BRANCHES["mozilla-2.1"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-2.1"]["enable_release"] = True
BRANCHES["mozilla-2.1"]["release_config_file"] = "deb_repos/staging_4.0_release.json"
BRANCHES["mozilla-2.1"]["release_platforms"] = ["fremantle"]
BRANCHES["mozilla-2.1"]["nightly_hour"] = 9

BRANCHES["mozilla-mobile-5.0"]["script_repo_tag"] = "default"
BRANCHES["mozilla-mobile-5.0"]["nightly_config_file"] = "deb_repos/staging_mozilla-beta_nightly.json"
BRANCHES["mozilla-mobile-5.0"]["nightly_platforms"] = ["fremantle", "fremantle-qt"]
BRANCHES["mozilla-mobile-5.0"]["enable_release"] = True
BRANCHES["mozilla-mobile-5.0"]["release_config_file"] = "deb_repos/staging_5.0_release.json"
BRANCHES["mozilla-mobile-5.0"]["release_platforms"] = ["fremantle"]
BRANCHES["mozilla-mobile-5.0"]["nightly_hour"] = 9
