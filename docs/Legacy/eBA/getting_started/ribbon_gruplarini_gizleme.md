# Ribbon Gruplarını Gizleme

Aşağıdaki kod ile RibbonBar'da yer alan gruplar gizlenebilir. 

	public void formRibbonGroupVisibilty(bool visible,string groupName) 

	        { 

	             RibbonGroup formGroup = RibbonBar.FindGroup(groupName); 

	            if (formGroup != null) 

	            { 

	                formGroup.Visible = visible; 

	            } 

	        } 

	protected override void OnLoad(EventArgs e) 

	        { 

	            base.OnLoad(e); 

	            formRibbonGroupVisibilty(false,"Share"); 

	            formRibbonGroupVisibilty(false,"Open"); 

	formRibbonGroupVisibilty(false,"Editing"); 

	}