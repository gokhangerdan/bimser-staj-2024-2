# Form Üzerinden Daha Önce Oluşturulmuş Akışa Ulaşma

Form üzerinden daha önce üretilmiş bir akışa aşağıdaki şekilde ulaşabilirsiniz.

```
this.openProcess({
                            projectName: "Project1",
                            processId: args.targetArgs.row.data.ProcessID,
                            processRequestId: "",
                            typeName: "OpenFormArgs",
                            parameters: [],
                            showOn: "drawer",
                            size: 2
                        });
```

