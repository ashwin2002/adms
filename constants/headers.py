class Gstr2(object):
    GSTIN = "GSTIN"
    DUMMY = "dummy"


class B2B(Gstr2):
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

    @staticmethod
    def get_dict():
        d = dict()
        d.update(vars(Gstr2))
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


class ExcelHeaders(object):
    input_header = dict()
    output_header = dict()

    # Input headers
    input_header["B2B"] = [
        B2B.GSTIN, B2B.SUPP_NAME, B2B.INV_NO, B2B.INV_TYPE, B2B.INV_DATE,
        B2B.INV_VALUE, B2B.PLACE, B2B.RCM, B2B.RATE, B2B.TAXABLE,
        B2B.IGST_PAID, B2B.CGST_PAID, B2B.SGST_PAID, B2B.CESS_PAID,
        B2B.SUBMITTED]

    input_header["B2BA"] = [
        Gstr2.DUMMY, Gstr2.DUMMY, B2BA.GSTIN, B2BA.SUPP_NAME,
        B2BA.INV_TYPE, B2BA.INV_NO, B2BA.INV_DATE, B2BA.INV_VALUE, B2BA.PLACE,
        B2BA.RCM, B2BA.RATE, B2BA.TAXABLE, B2BA.IGST_PAID, B2BA.CGST_PAID,
        B2BA.SGST_PAID, B2BA.CESS_PAID, B2BA.SUBMITTED]

    input_header["CDNR"] = [
        CDNR.GSTIN, CDNR.SUPP_NAME, CDNR.INV_TYPE, CDNR.INV_NO, CDNR.DUMMY,
        CDNR.INV_DATE, CDNR.INV_VALUE, CDNR.PLACE, CDNR.RCM,
        CDNR.RATE, CDNR.TAXABLE, CDNR.IGST_PAID, CDNR.CGST_PAID,
        CDNR.SGST_PAID, CDNR.CESS_PAID, CDNR.SUBMITTED]

    input_header["CDNRA"] = [
        CDNRA.INV_TYPE, CDNRA.INV_NO, CDNRA.INV_DATE, CDNRA.GSTIN,
        CDNRA.SUPP_NAME, CDNRA.INV_TYPE, CDNRA.INV_DATE, CDNRA.INV_NO,
        CDNRA.INV_VALUE, CDNRA.PLACE, CDNRA.RATE, CDNRA.TAXABLE,
        CDNRA.IGST_PAID, CDNRA.CGST_PAID, CDNRA.SGST_PAID, CDNRA.CESS_PAID,
        CDNRA.SUBMITTED]

    # Output headers
    output_header['B2B'] = [
        B2B.GSTIN, B2B.INV_NO, B2B.INV_DATE, B2B.INV_VALUE, B2B.PLACE,
        B2B.RCM, B2B.INV_TYPE, B2B.RATE, B2B.TAXABLE, B2B.IGST_PAID,
        B2B.CGST_PAID, B2B.SGST_PAID, B2B.CESS_PAID, B2B.ELIGIBLE,
        B2B.IGST_AVAILED, B2B.CGST_AVAILED, B2B.SGST_AVAILED,
        B2B.CESS_AVAILED, B2B.DOWNLOAD, B2B.GST2_YRM, B2B.SUPP_NAME,
        B2B.SUBMITTED]

    output_header['B2BA'] = [
        B2BA.GSTIN, B2BA.SUPP_NAME, B2BA.INV_NO, B2BA.INV_DATE, '', '',
        B2BA.INV_VALUE, B2BA.PLACE, B2BA.RCM, B2BA.INV_TYPE, B2BA.RATE,
        B2BA.TAXABLE, B2BA.IGST_PAID, B2BA.CGST_PAID, B2BA.SGST_PAID,
        B2BA.CESS_PAID, B2BA.IGST_AVAILED, B2BA.CGST_AVAILED,
        B2BA.SGST_AVAILED, B2BA.CESS_AVAILED, B2BA.DOWNLOAD_DATE,
        B2BA.GST2_YRM, B2BA.SUBMITTED]

    output_header['CDNR'] = [
        CDNR.GSTIN, CDNR.SUPP_NAME, CDNR.INV_TYPE, CDNR.INV_NO, '',
        CDNR.INV_DATE, CDNR.INV_VALUE, CDNR.PLACE, CDNR.RCM,
        CDNR.RATE, CDNR.TAXABLE, CDNR.IGST_PAID, CDNR.CGST_PAID,
        CDNR.SGST_PAID, CDNR.CESS_PAID, CDNR.SUBMITTED]

    output_header['CDNRA'] = [
        CDNRA.GSTIN, CDNRA.SUPP_NAME, CDNRA.INV_TYPE, CDNRA.INV_NO,
        CDNRA.INV_DATE, '', '', '', CDNRA.INV_VALUE, CDNRA.PLACE, '',
        CDNRA.RATE, CDNRA.TAXABLE, CDNRA.IGST_PAID, CDNRA.CGST_PAID,
        CDNRA.SGST_PAID, CDNRA.SUBMITTED]
