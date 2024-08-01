# Ribbon Buton Örnekleri

eBA Formlarında yer alan RibbonBar ile ilgili yapılabilecek işleler aşağıdaki gibidir.

	protected override void OnLoad(EventArgs e) 

	        { 

	            base.OnLoad(e); 

	            RibbonButton btnCheckOut = RibbonBar.FindButton("Editing", "CheckOut");//Editing grubuna ait checkout buttonu 

	            RibbonButton btnButton1 = RibbonBar.FindButton("EventButtons", "NewButton1"); //Event Button grubuna yeni eklenecek button 

	            RibbonButton btnButton2 = RibbonBar.FindButton("NewGroup1", "NewButton2"); //Yeni eklenen gruba eklenecek button 

	  

	  

	            RibbonGroup grpEdit = RibbonBar.FindGroup("Editing"); 

	            RibbonButton btnSave = RibbonBar.FindButton("Editing", "Save"); 

	            RibbonButton btnCancel = RibbonBar.FindButton("Editing", "Cancel"); 

	            RibbonGroup grpOpen = RibbonBar.FindGroup("Open"); 

	            RibbonGroup grpShare = RibbonBar.FindGroup("Share"); 

	            RibbonGroup grpEventButtons = RibbonBar.FindGroup("EventButtons"); 

	            RibbonGroup grpNewGroup1 = RibbonBar.FindGroup("NewGroup1"); //Yeni eklenecek grup. 

	  

	            //Button ayarları 

	            if (btnCheckOut != null) 

	            { 

	                btnCheckOut.VisibleIndex = 0; 

	                btnCheckOut.Count = 5; 

	                btnCheckOut.Visible = true; 

	                btnCheckOut.OnClickMethod = RibbonButton_onClickEvent2; 

	                btnCheckOut.Size = "big"; 

	            } 

	  

	            else 

	            { 

	                //Button eventlerinin çalışması için OnLoad içerisinde her seferinde atanması gerekir. 

	                btnCheckOut.OnClickMethod = RibbonButton_onClickEvent2; 

	            } 

	  

	            if (btnSave != null) 

	            { 

	                btnSave.VisibleIndex = 1; 

	            } 

	  

	            if (btnCancel != null) 

	            { 

	                btnCancel.VisibleIndex = 2; 

	            } 

Grup ayarları

	if (grpOpen != null) 

	                grpOpen.VisibleIndex = 0; 

	  

	            if (grpShare != null) 

	                grpShare.VisibleIndex = 1; 

	  

	            if (grpEdit != null) 

	            { 

	                grpEdit.VisibleIndex = 2; 

	                grpEdit.Caption = "E--D--I--T--I--N--G"; 

	                grpEdit.BackgroundColor = "rgba(255, 223, 104, 0.73)"; 

	            } 

	  

	            if (grpEventButtons != null) 

	            { 

	                grpEventButtons.VisibleIndex = 3; 

	            } 

Var olan gruba yeni button ekleme

	  if (btnButton1 == null && grpEventButtons != null && grpEventButtons.Buttons != null) 

	            { 

	                grpEventButtons.Buttons.Add(new RibbonButton() 

	                { 

	                    Caption = "NewButton1", 

	                    IconCode = "1027", 

	                    IconColor = "blue", 

	                    Name = "NewButton1", 

	                    Size = "small", 

	                    Visible = true, 

	                    VisibleIndex = 99, 

	                    OnClickMethod = RibbonButton_onClickEvent3, 

	                }); 

	            } 

	            else 

	            { 

	                //Button eventlerinin çalışması için OnLoad içerisinde her seferinde atanması gerekir. 

	                btnButton1.OnClickMethod = RibbonButton_onClickEvent4; 

	            } 

İçinde bir tane button olan yeni grup ekleme.

	  if (grpNewGroup1 == null) 

	            { 

	                RibbonGroup g = new RibbonGroup(); 

	                g.Name = "NewGroup1"; 

	                g.Caption = "NewGroup1"; 

	                g.Visible = true; 

	                g.BackgroundColor = "red"; 

	                g.VisibleIndex = 2; 

	  

	                RibbonButton btn = new RibbonButton() 

	                { 

	                    Caption = "NewButton2", 

	                    IconCode = "1027", 

	                    IconColor = "blue", 

	                    Name = "NewButton2", 

	                    Size = "big", 

	                    Visible = true, 

	                    OnClickMethod = RibbonButton_onClickEvent3, 

	                }; 

	  

	                g.Buttons.Add(btn); 

	  

	                RibbonBar.RibbonGroups.Add(g); 

	            } 

	  

	            else 

	            { 

	                //Button eventlerinin çalışması için OnLoad içerisinde her seferinde atanması gerekir. 

	                RibbonBar.FindButton("NewGroup1", "NewButton2").OnClickMethod = RibbonButton_onClickEvent3; 

	            } 

	             

	        } 

	         

	         

	                               public void Button1_OnClick(Object sender, EventArgs e) 

	                               { 

	                                

	                                   if(RibbonBar.FindButton("Editing","CheckOut") != null){ 

	                 RibbonBar.FindButton("Editing","CheckOut").Count = 6; 

	                 RibbonBar.FindButton("Editing","CheckOut").OnClickMethod = RibbonButton_onClickEvent2;  

	                 RibbonBar.FindButton("Editing","CheckOut").Visible = true; 

	            } 

	             

	            if(RibbonBar.FindGroup("Editing") != null){ 

	                 RibbonBar.FindGroup("Editing").Caption = "editing__"; 

	            } 

	             

	            if(RibbonBar.FindGroup("Open") != null){ 

	                 //RibbonBar.FindGroup("Open").Visible = false; 

	                 RibbonBar.FindGroup("Open").BackgroundColor = "red"; 

	            } 

	             

	            if(RibbonBar.FindGroup("Share") != null) { 

	                 RibbonBar.FindGroup("Share").BackgroundColor = "yellow"; 

	            } 

	               

	            if(RibbonBar.FindButton("Share","Print") != null){ 

	                 RibbonBar.FindButton("Share","Print").IconColor = "red"; 

	            } 

	             

	            if(RibbonBar.FindButton("Open","Notes") != null){ 

	                RibbonBar.FindButton("Open","Notes").IconColor = "yellow"; 

	            } 

	                 

	            if(RibbonBar.FindGroup("Open") != null) 

	                RibbonBar.FindGroup("Open").VisibleIndex = 1;   

	                  

	            if(RibbonBar.FindGroup("Share") != null) 

	                RibbonBar.FindGroup("Share").VisibleIndex = 0;  

	                 

	                   

	} 

	         

	        private void RibbonButton_onClickEvent2(EventArgs e) 

	        { 

	             txtFrom.Text = "CheckOut button clicked!";  

	        } 

	         

	        private void RibbonButton_onClickEvent3(EventArgs e) 

	        { 

	             txtFrom.Text = "NewButton2 clicked !";  

	        } 

	         

	        private void RibbonButton_onClickEvent4(EventArgs e) 

	        { 

	             txtFrom.Text = "NewButton1 clicked !";  

	        }