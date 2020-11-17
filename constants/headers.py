class Gstr(object):
    DUMMY = "dummy"

    GSTIN = "GSTIN"
    SUPP_NAME = "SuppName"
    INV_NO = "INVNo"
    INV_DATE = "INVDate"
    INV_VALUE = "INVValue"
    INV_TYPE = "INVType"
    REASON = "Reason"


class B2B(Gstr):
    PLACE = "Place"
    RCM = "RCM"
    RATE = "Rate"
    TAXABLE = "Taxable"
    IGST_PAID = "IGSTPaid"
    CGST_PAID = "CGSTPaid"
    SGST_PAID = "SGSTPaid"
    CESS_PAID = "CESSPaid"
    ELIGIBLE = "Eligible"
    IGST_AVAILED = "IGSTAVAILD"
    CGST_AVAILED = "CGSTAVAILD"
    SGST_AVAILED = "SGSTAVAILD"
    CESS_AVAILED = "CESSAVAILD"
    DOWNLOAD = "DWNLOAD"
    GST2_YRM = "GST2YRM"
    SUBMITTED = "Submitted"
    GSTR1_FILED_DATE = "GSTR1FiledDate"
    GST1_YRM = "GST1YRM"
    GST3_YRM = "GST3YRM"
    AMENDMENT = "Amendment"
    TAX_PERIOD = "TaxPeriod"
    EFFECTIVE_CANCELLATION_DATE = "EffCancelDate"
    PORT_CODE = "PortCode"
    TCS_NET = "TcsNet"
    APPLICABLE_TAX_RATE = "ApplicableTaxRate"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(vars(Gstr))
        d.update(vars(B2B))
        return d


class B2BA(B2B):
    DOWNLOAD_DATE = "DownloadDate"

    @staticmethod
    def get_dict():
        d = dict()
        d.update(B2B.get_dict())
        d.update(vars(B2BA))
        return d


class CDNR(B2BA):
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
