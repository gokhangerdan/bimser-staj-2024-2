Tetikleyen:

```
this.createForm({
	projectName: "",
	formName: "Form2",
	typeName: "CreateFormArgs",
	view: "default",
	size: 2,
	parameters:[
	{name: "prm1", type: "string", value: "testdeger" },
	{name: "prm2", type: "string", value: "testdeger2" }
	]
});
```

Karşılayan:

```
async Form2_OnLoad(args: Controls.EventArgs.ILoadEventArgs) {
	this.TextBox1.text=this.responseParameters['prm1'];
	this.TextBox2.text=this.responseParameters['prm2'];
}
```
