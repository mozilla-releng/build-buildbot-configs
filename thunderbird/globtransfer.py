#Override MozillaStageUpload to allow user-specified glob patterns for what to upload

from buildbotcustom.steps.transfer import MozillaStageUpload

class MozillaStageUploadGlob(MozillaStageUpload):
    def __init__(self, packageGlob=None, **kwargs):
        MozillaStageUpload.__init__(self, packageGlob=packageGlob, **kwargs)
        self.packageGlob = packageGlob
    def getPackageGlob(self):
        if self.packageGlob:
            return self.packageGlob
        else:
            return MozillaStageUpload.getPackageGlob(self)
