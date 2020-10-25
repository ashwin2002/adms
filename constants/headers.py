class Gstr(object):
    GSTIN = "GSTIN"
    DUMMY = "dummy"


class B2B(Gstr):
    SUPP_NAME = "SUPP_NAME"
    INV_NO = "INV_NO"
    INV_DATE = "INV_DATE"
    INV_VALUE = "INV_VALUE"
    PLACE = "Place"
    RCM = "RCM"
    INV_TYPE = "INV_TYPE"
    RATE = "Rate"
    TAXABLE = "Taxable"
    IGST_PAID = "IGST_Paid"
    CGST_PAID = "CGST_Paid"
    SGST_PAID = "SGST_Paid"
    CESS_PAID = "CESS_Paid"
    ELIGIBLE = "Eligible"
    IGST_AVAILED = "IGST_AVAILD"
    CGST_AVAILED = "CGST_AVAILD"
    SGST_AVAILED = "SGST_AVAILD"
    CESS_AVAILED = "CESS_AVAILD"
    DOWNLOAD = "DWNLOAD"
    GST2_YRM = "GST2YRM"
    SUBMITTED = "Submitted"
    GSTR1_FILED_DATE = "GSTR1_FILED_DATE"
    GST1_YRM = "GST1YRM"
    GST3_YRM = "GST3YRM"
    AMENDMENT = "Amendment"
    TAX_PERIOD = "TAX_PERIOD"
    EFFECTIVE_CANCELLATION_DATE = "EFF_CANCEL_DATE"
    PORT_CODE = "PORT_CODE"
    TCS_NET = "TCS_NET"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(vars(Gstr))
        d.update(vars(B2B))
        return d


class B2BA(B2B):
    DOWNLOAD_DATE = "Download_date"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(B2BA))
        return d


class CDNR(B2BA):
    INV_TYPE = "Note Type"
    REASON = "Reason"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2BA.get_dict())
        d.update(vars(CDNR))
        return d


class CDNRA(CDNR):
    @staticmethod
    def get_dict():
        d = dict()
        d.update(CDNR.get_dict())
        d.update(vars(CDNRA))
        return d


class TDS(B2B):
    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(TDS))
        return d


class TCS(B2B):
    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(TCS))
        return d


class IMPG(B2B):
    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(IMPG))
        return d
