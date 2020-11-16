from collections import OrderedDict

from constants.headers import B2B, B2BA, CDNR, CDNRA, IMPG, TDS, TCS


class Gstr2HeadersTillJun2020(object):
    input_header = OrderedDict()
    output_header = dict()
    start_row = dict()

    start_row["B2B"] = 7
    start_row["B2BA"] = 8
    start_row["CDNR"] = 7
    start_row["CDNRA"] = 8

    # Input headers
    input_header["B2B"] = [
        B2B.GSTIN, B2B.SUPP_NAME, B2B.INV_NO, B2B.INV_TYPE, B2B.INV_DATE,
        B2B.INV_VALUE, B2B.PLACE, B2B.RCM, B2B.RATE, B2B.TAXABLE,
        B2B.IGST_PAID, B2B.CGST_PAID, B2B.SGST_PAID, B2B.CESS_PAID,
        B2B.SUBMITTED]

    input_header["B2BA"] = [
        B2BA.DUMMY, B2BA.DUMMY, B2BA.GSTIN, B2BA.SUPP_NAME,
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
        B2BA.GSTIN, B2BA.SUPP_NAME, B2BA.INV_NO, B2BA.INV_DATE,
        B2BA.INV_VALUE, B2BA.PLACE, B2BA.RCM, B2BA.INV_TYPE, B2BA.RATE,
        B2BA.TAXABLE, B2BA.IGST_PAID, B2BA.CGST_PAID, B2BA.SGST_PAID,
        B2BA.CESS_PAID, B2BA.IGST_AVAILED, B2BA.CGST_AVAILED,
        B2BA.SGST_AVAILED, B2BA.CESS_AVAILED, B2BA.DOWNLOAD_DATE,
        B2BA.GST2_YRM, B2BA.SUBMITTED]

    output_header['CDNR'] = [
        CDNR.GSTIN, CDNR.SUPP_NAME, CDNR.INV_TYPE, CDNR.INV_NO,
        CDNR.INV_DATE, CDNR.INV_VALUE, CDNR.PLACE, CDNR.RCM,
        CDNR.RATE, CDNR.TAXABLE, CDNR.IGST_PAID, CDNR.CGST_PAID,
        CDNR.SGST_PAID, CDNR.CESS_PAID, CDNR.SUBMITTED]

    output_header['CDNRA'] = [
        CDNRA.GSTIN, CDNRA.SUPP_NAME, CDNRA.INV_TYPE, CDNRA.INV_NO,
        CDNRA.INV_DATE, CDNRA.INV_VALUE, CDNRA.PLACE,
        CDNRA.RATE, CDNRA.TAXABLE, CDNRA.IGST_PAID, CDNRA.CGST_PAID,
        CDNRA.SGST_PAID, CDNRA.SUBMITTED]

    dbf_spec = "GSTIN C(18); INVNO C(16); INVDATE D; INVVALUE N(15,2); " \
               "PLACE C(11); RCM C(5); INVTYPE C(8); RATE N(15,2); " \
               "TAXABLE N(15,2); IGSTPAID N(15,2); CGSTPAID N(15,2); " \
               "SGSTPAID N(15,2); CESSPAID N(15,2); ELIGIBLE C(15); " \
               "IGSTAVAILD N(15,2); CGSTAVAILD N(15,2); SGSTAVAILD N(15,2); " \
               "CESSAVAILD N(15,2); DWNLOAD D, GST2YRM C(9); " \
               "SUPPNAME C(35); SUBMITTED C(11)"


class Gstr2HeadersJul2020Current(object):
    input_header = OrderedDict()
    output_header = dict()
    start_row = dict()

    start_row["B2B"] = 7
    start_row["B2BA"] = 8
    start_row["CDNR"] = 7
    start_row["CDNRA"] = 8
    start_row["TDS"] = 7
    start_row["TCS"] = 7
    start_row["IMPG"] = 7

    # Input headers
    input_header["B2B"] = [
        B2B.GSTIN, B2B.SUPP_NAME, B2B.INV_NO, B2B.INV_TYPE, B2B.INV_DATE,
        B2B.INV_VALUE, B2B.PLACE, B2B.RCM, B2B.RATE, B2B.TAXABLE,
        B2B.IGST_PAID, B2B.CGST_PAID, B2B.SGST_PAID, B2B.CESS_PAID,
        B2B.SUBMITTED, B2B.GSTR1_FILED_DATE, B2B.GST1_YRM, B2B.GST3_YRM,
        B2B.AMENDMENT, B2B.TAX_PERIOD, B2B.EFFECTIVE_CANCELLATION_DATE]

    input_header["B2BA"] = [
        B2BA.DUMMY, B2BA.DUMMY, B2BA.GSTIN, B2BA.SUPP_NAME,
        B2BA.INV_TYPE, B2BA.INV_NO, B2BA.INV_DATE, B2BA.INV_VALUE, B2BA.PLACE,
        B2BA.RCM, B2BA.RATE, B2BA.TAXABLE, B2BA.IGST_PAID, B2BA.CGST_PAID,
        B2BA.SGST_PAID, B2BA.CESS_PAID, B2BA.SUBMITTED, B2BA.GSTR1_FILED_DATE,
        B2BA.GST1_YRM, B2BA.GST3_YRM, B2BA.EFFECTIVE_CANCELLATION_DATE,
        B2BA.AMENDMENT, B2BA.TAX_PERIOD]

    input_header["CDNR"] = [
        CDNR.GSTIN, CDNR.SUPP_NAME, CDNR.INV_TYPE, CDNR.INV_NO,
        CDNR.INV_DATE, CDNR.INV_VALUE, CDNR.REASON, CDNR.RATE,
        CDNR.TAXABLE, CDNR.IGST_PAID, CDNR.CGST_PAID, CDNR.SGST_PAID,
        CDNR.CESS_PAID, CDNR.DUMMY, CDNR.SUBMITTED, CDNR.GSTR1_FILED_DATE,
        CDNR.GST1_YRM, CDNR.GST3_YRM, CDNR.AMENDMENT,
        CDNR.EFFECTIVE_CANCELLATION_DATE, CDNR.DUMMY, CDNR.RCM, CDNR.PLACE]

    input_header["CDNRA"] = [
        CDNRA.INV_TYPE, CDNRA.INV_NO, CDNRA.INV_DATE, CDNRA.GSTIN,
        CDNRA.SUPP_NAME, CDNRA.INV_TYPE, CDNRA.INV_NO, CDNRA.INV_TYPE,
        CDNRA.INV_DATE, CDNRA.INV_VALUE, CDNRA.PLACE, CDNRA.RCM,
        CDNRA.RATE, CDNRA.TAXABLE, CDNRA.IGST_PAID, CDNRA.CGST_PAID,
        CDNRA.SGST_PAID, CDNRA.CESS_PAID, CDNRA.SUBMITTED,
        CDNRA.GSTR1_FILED_DATE, CDNRA.GST1_YRM, CDNRA.GST3_YRM,
        CDNRA.AMENDMENT, CDNRA.TAX_PERIOD, CDNRA.EFFECTIVE_CANCELLATION_DATE]

    input_header["TDS"] = [
        TDS.GSTIN, TDS.SUPP_NAME, TDS.GST2_YRM, TDS.TAXABLE,
        TDS.IGST_PAID, TDS.CGST_PAID, TDS.SGST_PAID]

    input_header["TCS"] = [
        TCS.GSTIN, TCS.SUPP_NAME, TCS.GST2_YRM, TCS.INV_VALUE,
        TCS.TAXABLE, TCS.TCS_NET,
        TCS.IGST_PAID, TCS.CGST_PAID, TCS.SGST_PAID]

    input_header["IMPG"] = [
        IMPG.GSTR1_FILED_DATE, IMPG.PORT_CODE, IMPG.INV_NO, IMPG.INV_DATE,
        IMPG.TAXABLE, IMPG.IGST_PAID, IMPG.CESS_PAID, IMPG.AMENDMENT]

    # Output headers
    output_header['B2B'] = [
        B2B.GSTIN, B2B.INV_NO, B2B.INV_DATE, B2B.INV_VALUE, B2B.PLACE,
        B2B.RCM, B2B.INV_TYPE, B2B.RATE, B2B.TAXABLE, B2B.IGST_PAID,
        B2B.CGST_PAID, B2B.SGST_PAID, B2B.CESS_PAID, B2B.ELIGIBLE,
        B2B.IGST_AVAILED, B2B.CGST_AVAILED, B2B.SGST_AVAILED,
        B2B.CESS_AVAILED, B2B.DOWNLOAD, B2B.GST2_YRM, B2B.SUPP_NAME,
        B2B.SUBMITTED, B2B.GSTR1_FILED_DATE, B2B.GST1_YRM, B2B.GST3_YRM,
        B2B.AMENDMENT, B2B.TAX_PERIOD, B2B.EFFECTIVE_CANCELLATION_DATE,
        B2B.TCS_NET, B2B.PORT_CODE]

    output_header['B2BA'] = input_header['B2BA']
    output_header['CDNR'] = input_header['CDNR']
    output_header['CDNRA'] = input_header['CDNRA']
    output_header['TDS'] = input_header['TDS']
    output_header['TCS'] = input_header['TCS']
    output_header["IMPG"] = [
        IMPG.GSTIN, IMPG.SUPP_NAME, IMPG.GSTR1_FILED_DATE, IMPG.PORT_CODE,
        IMPG.INV_NO, IMPG.INV_DATE, IMPG.TAXABLE, IMPG.IGST_PAID,
        IMPG.CESS_PAID, IMPG.INV_VALUE, IMPG.SUBMITTED, IMPG.GST1_YRM,
        IMPG.GST3_YRM, IMPG.AMENDMENT]

    dbf_spec = "GSTIN C(18); INVNO C(16); INVDATE D; INVVALUE N(15,2); " \
               "PLACE C(11); RCM C(5); INVTYPE C(8); RATE N(15,2); " \
               "TAXABLE N(15,2); IGSTPAID N(15,2); CGSTPAID N(15,2); " \
               "SGSTPAID N(15,2); CESSPAID N(15,2); ELIGIBLE C(15); " \
               "IGSTAVAILD N(15,2); CGSTAVAILD N(15,2); SGSTAVAILD N(15,2); " \
               "CESSAVAILD N(15,2); DWNLOAD D; GST2YRM C(9); " \
               "SUPPNAME C(35); SUBMITTED C(11); GSTR1FILED C(9); " \
               "GST1YRM C(9); GST3YRM C(9); AMENDMENT C(9); TAXPERIOD C(9); " \
               "EFFCANCELD C(9); TCS_NET C(9); PORT_CODE C(9)"
