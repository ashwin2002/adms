class Gstr(object):
    GSTIN = "GSTIN"
    DUMMY = "dummy"


class B2B(Gstr):
    SUPP_NAME = "SUPPNAME"
    INV_NO = "INVNO"
    INV_DATE = "INVDATE"
    INV_VALUE = "INVVALUE"
    PLACE = "PLACE"
    RCM = "RCM"
    INV_TYPE = "INVTYPE"
    RATE = "RATE"
    TAXABLE = "TAXABLE"
    IGST_PAID = "IGSTPAID"
    CGST_PAID = "CGSTPAID"
    SGST_PAID = "SGSTPAID"
    CESS_PAID = "CESSPAID"
    ELIGIBLE = "ELIGIBLE"
    IGST_AVAILED = "IGSTAVAILD"
    CGST_AVAILED = "CGSTAVAILD"
    SGST_AVAILED = "SGSTAVAILD"
    CESS_AVAILED = "CESSAVAILD"
    DOWNLOAD = "DWNLOAD"
    GST2_YRM = "GST2YRM"
    SUBMITTED = "SUBMITTED"
    GSTR1_FILLED_DATE = "GSTR1FILEDDATE"
    GST1_YRM = "GST1YRM"
    GST3_YRM = "GST3YRM"
    AMENDMENT = "AMENDMENT"
    TAX_PERIOD = "TAXPERIOD"
    EFFECTIVE_CANCELLATION_DATE = "EFFCANCELDATE"
    PORT_CODE = "PORT_CODE"
    TCS_NET = "TCS_NET"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(vars(Gstr))
        d.update(vars(B2B))
        return d


class B2BA(B2B):
    INV_NO = "INV No"
    INV_DATE = "INV Date"
    INV_VALUE = "INV Value"
    INV_TYPE = "INV Type"
    PLACE = "Place"
    RATE = "Rate"
    TAXABLE = "Taxable"
    IGST_PAID = "IGST"
    CGST_PAID = "CGST"
    SGST_PAID = "SGST"
    CESS_PAID = "CESS"
    IGST_AVAILED = "IGST availed"
    CGST_AVAILED = "CGST availed"
    SGST_AVAILED = "SGST availed"
    CESS_AVAILED = "CESS availed"
    DOWNLOAD_DATE = "Download date"
    SUBMITTED = "Submitted"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(B2BA))
        return d


class CDNR(B2BA):
    INV_TYPE = "Note Type"
    SUPP_NAME = "SUPP Name"
    REASON = "Reason"
    IGST_PAID = "IGST Paid"
    CGST_PAID = "CGST Paid"
    SGST_PAID = "SGST Paid"
    CESS_PAID = "CESS Paid"

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
