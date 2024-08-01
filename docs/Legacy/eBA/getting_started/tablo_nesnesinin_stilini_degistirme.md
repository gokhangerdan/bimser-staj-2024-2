# Tablo Nesnesinin Stil'ini değiştirme

	override protected void internalOnPageLoad(Object sender, EventArgs e) 

	        { 

	            base.internalOnPageLoad(sender,e); 

	            Table1.RenderCell+=Table1_RenderCell;             

	        } 

	        public void Table1_RenderCell(object sender, eBATableRenderCellArgs args) 

	        { 

	            if (args.CellType==eBATableCellType.Header) 

	                args.Style+="color:red;width:120px;height:120px;";                  

	        }