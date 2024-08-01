# ToolBarButton Gizleme

Aşağıdaki kodla Form server tarafında bir ToolbarButton gizlenebilir.

	ToolbarButtons.Find(x=>x.Name=="button_Adi").Enabled = false;