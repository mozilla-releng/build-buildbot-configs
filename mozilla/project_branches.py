# Additional branches that start as identical (individual variables can be overriden here)
PROJECT_BRANCHES = {
    'build-system': {},
    'services-central': {
        'repo_path': 'services/services-central',
    },
    'maple': {},
    'cedar': {},
    'birch': {},
}

# Load up project branches' local values
for branch in PROJECT_BRANCHES.keys():
    PROJECT_BRANCHES[branch]['tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['mobile_tinderbox_tree'] = branch.title()
    PROJECT_BRANCHES[branch]['packaged_unittest_tinderbox_tree'] = branch.title()
