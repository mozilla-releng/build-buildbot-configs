SLAVES = {
    "linux": ["debsign1"],
}

BRANCHES = {
    "mozilla-beta": {},
    "mozilla-release": {},
}
BRANCHES["mozilla-beta"]["script_repo_tag"] = 'default'
BRANCHES["mozilla-beta"]["enable_nightly"] = False
BRANCHES["mozilla-beta"]["enable_release"] = True
BRANCHES["mozilla-beta"]["release_config_file"] = "deb_repos/release_mozilla-beta.py"
BRANCHES["mozilla-beta"]["release_platforms"] = ["fremantle"]

BRANCHES["mozilla-release"]["script_repo_tag"] = 'default'
BRANCHES["mozilla-release"]["enable_nightly"] = False
BRANCHES["mozilla-release"]["enable_release"] = True
BRANCHES["mozilla-release"]["release_config_file"] = "deb_repos/release_mozilla-release.py"
BRANCHES["mozilla-release"]["release_platforms"] = ["fremantle"]
