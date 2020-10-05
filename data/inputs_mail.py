mail_info = dict()
mail_info["itc_na"] = dict()
mail_info["gstr2_only"] = dict()

# Mail subject
mail_info["itc_na"]["subject"] = "ITC-NA"
mail_info["gstr2_only"]["subject"] = "Available only in GSTR-2"

# Mail headings
mail_info["itc_na"]["heading"] = "Message from ADMS to %s"
mail_info["gstr2_only"]["heading"] = "Message from %s"

# Mail body
mail_info["itc_na"]["message"] = "Inputs not given by the supplier: " \
                                 "If already filed Kindly ignore this mail"
mail_info["gstr2_only"]["message"] = "Please collect the said Bills:"

mail_info["html_header"] = """
<html>
  <head></head>
  <body>
    <p>
        %s
    </p>
    
    </br>
    
    <p>Dear Sir/s,</br>
       Please look into the following,</br>
       %s
    </p>
    <table border=1 style="border-collapse: collapse;">
      <tr>
        <th> Invoice_no </th>
        <th> Invoice_date </th>
        <th> Invoice_value </th>
        <th> Taxable_value </th>
        <th> IGST </th>
        <th> CGST </th>
        <th> SGST </th>
        <th> S_No. </th>
      </tr>
"""

mail_info["html_footer"] = """
    </table>
    <br/>
    <p>
      Thank you, </br>
      %s
    </p>
    <br/>
    <p>
      <b>Note:</b> 
      eMail sent based on GSTR-2 report downloaded from GST portal dated %s
    </p>
  </body>
</html>
"""

mail_info["table_tr_format"] = """
    <tr>
      <td> %s </td>
      <td> %s </td>
      <td align="right"> %.2f </td>
      <td align="right"> %.2f </td>
      <td align="right"> %.2f </td>
      <td align="right"> %.2f </td>
      <td align="right"> %.2f </td>
      <td> %s </td>
    </tr>
"""

mail_info["table_total_tr_format"] = """
    <tr>
      <td> </td>
      <td> </td>
      <td> </td>
      <td> <b> Total </b> </td>
      <td align="right"> <b> %.2f </b> </td>
      <td align="right"> <b> %.2f </b> </td>
      <td align="right"> <b> %.2f </b> </td>
      <td> </td>
    </tr>
"""
