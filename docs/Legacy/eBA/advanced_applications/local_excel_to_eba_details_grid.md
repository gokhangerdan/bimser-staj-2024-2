# Excel import

## eBA Sunucusundaki Excel dosyasının Detay Tabloya Aktarımı

___

eBA uygulama Sunucusunda Microsoft Access Database Engine 2016 kurulu olmalıdır.

___

Form açılır açılmaz windows uygulamanın kurulu olduğu sunucudaki windows klasöründe bulunan excel dosya içeriği detay tablo nesnesine aktarılması amaçlanmıştır.
onLoadData event'i içerisinde excel okunarak datatable'a aktarılır, harici fonksiyon ile datatable'daki veriler detay tabloya yazdırılır.

___

Detay tablo'daki 'Maximum Row Count' sayısı dikkate alınmalıdır.

___

Projeye eklenecek referans DLL

%SystemPath%\Common\eBADB.dll

___

using System;

using System.Collections;

using System.Text;

using System.Data;

using eBAControls;

using eBAControls.eBABaseForm;

using eBAFormData;

using System.Web.UI.WebControls;


using System.Data.OleDb;

using System.Data.SqlClient;

namespace Excel

{

    public partial class Form

    {

        public void OnLoadData()

        {

            string FileName = @"C:\BimserCozum\eBA\DMFiles\Sample.xlsx";

            string sheetName = "Sheet1$"; //Exceldeki okunacak sheet 

            DataTable dtResult = new DataTable();

            using (OleDbConnection objConn = new OleDbConnection(@"Provider=Microsoft.ACE.OLEDB.12.0;Data Source=" + FileName + ";Extended Properties='Excel 12.0;HDR=YES;IMEX=1;';"))

            {

                objConn.Open();

                OleDbCommand cmd = new OleDbCommand();

                OleDbDataAdapter oleda = new OleDbDataAdapter();

                cmd.Connection = objConn;

                cmd.CommandType = CommandType.Text;

                cmd.CommandText = "SELECT * FROM [" + sheetName + "]";

                oleda = new OleDbDataAdapter(cmd);

                oleda.Fill(dtResult);

                objConn.Close();

            }

            SaveDataDetailsGrid(dtResult);

        }

        public void SaveDataDetailsGrid(DataTable dtExcel)

        {

            try

            {

                if (dtExcel.Rows.Count > 0)

                {

                    for (int i = 0; i < dtExcel.Rows.Count; i++)

                    {

                        DetayTablo1.CurrentRowCount++;

                        ((TextBox)DetayTablo1.GetRowObject(i, "txtID")).Text = dtExcel.Rows[i]["ID"].ToString();

                        ((TextBox)DetayTablo1.GetRowObject(i, "txtName")).Text = dtExcel.Rows[i]["Name"].ToString();

                        ((TextBox)DetayTablo1.GetRowObject(i, "txtGender")).Text = dtExcel.Rows[i]["Gender"].ToString();

                    }

                }

            }

            catch (Exception ex)

            {

                throw new Exception(ex.Message);

            }

        }

    }

}



![](https://docsbimser.blob.core.windows.net/imagecontainer/Local%20Excel%20to%20eBA%20Details%20Grid-4503e4cb-1d35-4ecc-b3cb-a41599673109.png)

