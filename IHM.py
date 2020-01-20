from tkinter import *
import tkinter.ttk as ttk
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from Manifestation import *


def createList(limit):
    i = 0
    filterForDatas = list()
    while i < limit:
        filterForDatas.append(StringVar())
        i = i + 1
    return filterForDatas


class IHM(Frame):
    # region INIT Window root
    def __init__(self, data, root):
        Frame.__init__(self, root)
        self.root = root
        if data is None:
            data = [Manifestation()]
        self.data = data
        self.filterForDatas = createList(8)
        self.tree = ttk.Treeview()
        self.root.title("Python - Import CSV File To Tkinter Table")
        width = 1900
        height = 1040
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry("%dx%d+%d+%d" % (width, height, x, y))
        self.root.resizable(0, 0)
        filterForData = Frame(self.root)
        filterForData.pack(side=LEFT, anchor="n")
        label = Label(filterForData, text="FILTRE :")
        label.pack(fill=X)
        labelChamp = Label(filterForData, text="Nom de la manifestation :")
        labelChamp.pack(fill=X)
        entryChamp = Entry(filterForData, textvariable=self.filterForDatas[0])
        entryChamp.pack(fill=X)
        labelChamp1 = Label(filterForData, text="code postal :")
        labelChamp1.pack(fill=X)
        entryChamp1 = Entry(filterForData, textvariable=self.filterForDatas[1])
        entryChamp1.pack(fill=X)
        labelChamp2 = Label(filterForData, text="site web :")
        labelChamp2.pack(fill=X)
        entryChamp2 = Entry(filterForData, textvariable=self.filterForDatas[2])
        entryChamp2.pack(fill=X)
        labelChamp3 = Label(filterForData, text="date de début :")
        labelChamp3.pack(fill=X)
        entryChamp3 = Entry(filterForData, textvariable=self.filterForDatas[3])
        entryChamp3.pack(fill=X)
        labelChamp4 = Label(filterForData, text="date de fin :")
        labelChamp4.pack(fill=X)
        entryChamp4 = Entry(filterForData, textvariable=self.filterForDatas[4])
        entryChamp4.pack(fill=X)
        labelChamp5 = Label(filterForData, text="Commune principale :")
        labelChamp5.pack(fill=X)
        entryChamp5 = Entry(filterForData, textvariable=self.filterForDatas[5])
        entryChamp5.pack(fill=X)
        labelChamp6 = Label(filterForData, text="Domaine :")
        labelChamp6.pack(fill=X)
        entryChamp6 = Entry(filterForData, textvariable=self.filterForDatas[6])
        entryChamp6.pack(fill=X)
        labelChamp7 = Label(filterForData, text="Complément :")
        labelChamp7.pack(fill=X)
        entryChamp7 = Entry(filterForData, textvariable=self.filterForDatas[7])
        entryChamp7.pack(fill=X)
        buttonValide = Button(filterForData, text="Valider", command=self.refresh)
        buttonValide.pack(fill=X)
        buttonReset = Button(filterForData, text="Reset", command=self.reset)
        buttonReset.pack(fill=X)
        buttonSave = Button(filterForData, text="Save", anchor="s", command=self.popup)
        buttonSave.pack(fill=X)
        buttonQuit = Button(filterForData, text="Fermer", anchor="s", command=self.closeWindow)
        buttonQuit.pack(fill=X)
        TableMargin = Frame(self.root)
        TableMargin.pack()
        scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
        scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
        self.tree = ttk.Treeview(TableMargin, columns=(
            "Nom de la manifestation", "code postal", "site web", "date de début", "date de fin", "Commune principale",
            "Domaine", "Complément"), height=400,
                                 selectmode="extended",
                                 yscrollcommand=scrollbary.set,
                                 xscrollcommand=scrollbarx.set)
        scrollbary.config(command=self.tree.yview)
        scrollbary.pack(side=RIGHT, fill=Y)
        scrollbarx.config(command=self.tree.xview)
        scrollbarx.pack(side=BOTTOM, fill=X)
        self.tree.heading('Nom de la manifestation', text="Nom de la manifestation", anchor=W)
        self.tree.heading('code postal', text="code postal", anchor=W)
        self.tree.heading('site web', text="site web", anchor=W)
        self.tree.heading('date de début', text="date de début", anchor=W)
        self.tree.heading('date de fin', text="date de fin", anchor=W)
        self.tree.heading('Commune principale', text="Commune principale", anchor=W)
        self.tree.heading('Domaine', text="Domaine", anchor=W)
        self.tree.heading('Complément', text="Complément", anchor=W)
        self.tree.column('#0', stretch=YES, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=300)
        self.tree.column('#2', stretch=YES, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=300)
        self.tree.column('#4', stretch=NO, minwidth=0, width=100)
        self.tree.column('#5', stretch=YES, minwidth=0, width=100)
        self.tree.column('#6', stretch=YES, minwidth=0, width=300)
        self.tree.column('#7', stretch=YES, minwidth=0, width=300)
        self.tree.column('#8', stretch=YES, minwidth=0, width=300)
        self.tree.pack()

    # endregion

    # region INIT Window POPUP
    def popup(self):
        popup = Tk()
        check = IntVar(popup)
        popup.title("Sauvegarde")
        popup.geometry("%dx%d+%d+%d" % (300, 150, 300, 150))
        label_champ = Label(popup, text="Nom du fichier :")
        label_champ.pack(fill=X)
        fileName = Entry(popup)
        fileName.pack(fill=X)
        checkHTML = Radiobutton(popup, text="HTML", variable=check, value=1)
        checkHTML.pack(fill=X)
        checkPDF = Radiobutton(popup, text="PDF", variable=check, value=0)
        checkPDF.pack(fill=X)
        labelChamp1 = Label(popup, text="Chemin du fichier :")
        labelChamp1.pack(fill=X)
        filePath = Entry(popup)
        filePath.pack(fill=X)
        buttonValide = Button(popup, text="Valider", command=lambda: self.saveFile(popup,
                                                                                   check.get(),
                                                                                   fileName.get(),
                                                                                   filePath.get()))
        buttonValide.pack(fill=X)

    # endregion

    def saveFile(self, popup, check, name, path):
        if check == 1 and name != "" and path != "":
            self.saveFileAsHTML(name, path)
        elif check == 0 and name != "" and path != "":
            self.saveFileAsPDF(name, path)
        popup.destroy()

    # region Load Data into Object Tree or List
    def loadData(self, test):
        data = [["Nom de la manifestation", "Code postal", "Site web", "Date de début",
                 "Date de fin", "Commune principale", "Domaine", "Complément"]]
        for element in self.data:
            if element.getNomManifestation() == self.filterForDatas[0].get() \
                    or self.filterForDatas[0].get() == "":
                if element.getCodePostal() == self.filterForDatas[1].get() \
                        or self.filterForDatas[1].get() == "":
                    if element.getSiteWeb() == self.filterForDatas[2].get() \
                            or self.filterForDatas[2].get() == "":
                        if element.getDate()[0] == self.filterForDatas[3].get() \
                                or self.filterForDatas[3].get() == "":
                            if element.getDate()[1] == self.filterForDatas[4].get() \
                                    or self.filterForDatas[4].get() == "":
                                if element.getCommunePrincipal() == self.filterForDatas[5].get() \
                                        or self.filterForDatas[5].get() == "":
                                    if element.getDomaines().getDomaine() == self.filterForDatas[6].get() \
                                            or self.filterForDatas[6].get() == "":
                                        if element.getDomaines().getComplement() == self.filterForDatas[7].get() \
                                                or self.filterForDatas[7].get() == "":
                                            if test == 1:
                                                data.append([element.getNomManifestation(),
                                                             element.getCodePostal(),
                                                             element.getSiteWeb(),
                                                             element.getDate()[0],
                                                             element.getDate()[1],
                                                             element.getCommunePrincipal(),
                                                             element.getDomaines().getDomaine(),
                                                             element.getDomaines().getComplement()])
                                            elif test == 0:
                                                self.tree.insert("", 0, values=(
                                                    element.getNomManifestation(), element.getCodePostal(),
                                                    element.getSiteWeb(), element.getDate()[0],
                                                    element.getDate()[1], element.getCommunePrincipal(),
                                                    element.getDomaines().getDomaine(),
                                                    element.getDomaines().getComplement()))
        if test == 1:
            return (data)

    # endregion

    # region Save as PDF
    def saveFileAsPDF(self, name, path):
        fullData = self.loadData(1)
        doc = SimpleDocTemplate(path + "\\" + name + ".pdf", pagesize=A4)
        doc.pagesize = landscape(A4)
        elements = []
        style = TableStyle([('ALIGN', (1, 1), (-2, -2), 'RIGHT'),
                            ('TEXTCOLOR', (1, 1), (-2, -2), colors.red),
                            ('VALIGN', (0, 0), (0, -1), 'TOP'),
                            ('TEXTCOLOR', (0, 0), (0, -1), colors.blue),
                            ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
                            ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
                            ('TEXTCOLOR', (0, -1), (-1, -1), colors.green),
                            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
                            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
                            ])
        s = getSampleStyleSheet()
        s = s["BodyText"]
        s.wordWrap = 'CJK'
        data2 = [[Paragraph(cell, s) for cell in row] for row in fullData]
        t = Table(data2)
        t.setStyle(style)
        elements.append(t)
        print(data2)
        doc.build(elements)
        print("Test3")

    # endregion

    # region Save as HTML
    def saveFileAsHTML(self, name, path):
        i = 0
        file = open(path + "\\" + name + ".html", "a")
        data = self.loadData(1)
        for element in data:
            if i == 0:
                file.write("<table class=\"panorama-des-festivals\">"
                           "\n<thead>"
                           "\n\t<tr>"
                           "\n\t\t<th title=\"Field #1\">{}</th>"
                           "\n\t\t<th title=\"Field #2\">{}</th>"
                           "\n\t\t<th title=\"Field #3\">{}</th>"
                           "\n\t\t<th title=\"Field #4\">{}</th>"
                           "\n\t\t<th title=\"Field #5\">{}</th>"
                           "\n\t\t<th title=\"Field #6\">{}</th>"
                           "\n\t\t<th title=\"Field #7\">{}</th>"
                           "\n\t\t<th title=\"Field #8\">{}</th>"
                           "\n\t</tr>"
                           "\n</thead>"
                           "\n<tbody>".format(element[0],
                                              element[1],
                                              element[2],
                                              element[3],
                                              element[4],
                                              element[5],
                                              element[6],
                                              element[7]))
                i = i + 1
            elif i != 0:
                file.write("\n\t<tr>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t\t<td>{}</td>"
                           "\n\t</tr>".format(element[0],
                                              element[1],
                                              element[2],
                                              element[3],
                                              element[4],
                                              element[5],
                                              element[6],
                                              element[7]))
        file.write("\n\t</tbody>\n</table>")

    # endregion

    def refresh(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.loadData(0)

    def closeWindow(self):
        self.root.destroy()

    def reset(self):
        for element in self.filterForDatas:
            element.set("")

    def init_window(self):
        self.loadData(0)
        self.root.mainloop()
