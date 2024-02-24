"""Module providing a function printing python version."""
from flet import *
import flet as ft
from time import sleep
import mysql.connector

  # page.splash = ft.ProgressBar(visible=False)
#mydb = mysql.connector.connect(
#    host="localhost",
#    user="root",
#    password="65076507",
#    database="empresa0000",
#    port='3306'
#)eeeee

#mydb = mysql.connector.connect(
#   host="localhost",
#    user="root",
#    password="65076507",
#    database="empresa0000",
#    port='3306'
#)

mydb = mysql.connector.connect(
    host="198.199.69.147",
    user="userloc",
    password="UsL6507$#@!6507",
    database="empresa0000",
    port='3306'
)


pnIndex     = 0
pnAgrupro   = 0
pnAdic      = 0
pnCompany   = 0
    
def main(page: ft.Page):
    """Function printing python version."""
    page.theme_mode = 'light'
    page.scroll = "ADAPTIVE"
    page.window_min_height = 300
    page.window_center
    page.window_width = 340
    page.window_heigth = 570
    
    
  
    txt_number2 = ft.TextField(value="0", text_align="center", width=40)
    
    txt_gruagru = ft.TextField(value=0, text_align="left", width=100)
    
    txt_pedido  = ft.Text(value="X", text_align="left", width=300)

    
    
    
    page.add(txt_gruagru)
    
    
    def minus_click(e):
        txt_number2.value = str(int(txt_number2.value) - 1)
        page.update()

    def plus_click(e):
        txt_number2.value = str(int(txt_number2.value) + 1)
        page.update()

    
    
    mydt = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('Cardápio')),
            ft.DataColumn(ft.Text('Selecionar')),
 
        ]
    )
    
    mydt_produtos = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text('Descrição')),
            ft.DataColumn(ft.Text('Preço')),
            ft.DataColumn(ft.Text('Selecionar')),
            ft.DataColumn(ft.Text('Alterar')),
        ]
    )    
    
    #cursor = mydb.cursor()
    #cursor.execute("SELECT * FROM Produtos")
    #results = cursor.fetchall()
    
    def changetheme(e):
       # page.splash.visible = True
        page.theme_mode='light' if page.theme_mode=='dark' else 'dark'
        page.update()
        
        #sleep(1)
        toggledarklight.selected = not toggledarklight.selected
    
    toggledarklight=ft.IconButton(
        on_click=changetheme,
        icon="dark_mode",
        selected_icon="light_mode",
        style=ft.ButtonStyle(
            color={"":ft.colors.BLACK, 'selected': ft.colors.WHITE}
        )
    )

    def menu_inicio(e):
        print("menu_inicio 2 " )
        page.add(
            ft.AppBar(
                title=ft.Text('Comger APP' , size=20),
                bgcolor="blue",
                leading=ft.IconButton(icon="menu"),
                actions=[
                toggledarklight,
                ft.ElevatedButton("Cardápio (Grupos)", 
                    on_click=load_data),
                ]
            ),
        )   
        page.Bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
            ),
        )     
    
    
    # *************************************************************************************************** #
    def opendialog(e):
        page.title = "AlertDialog examples"
        print("opendialog")
        dlg = ft.AlertDialog(
            title=ft.Text("Hello, you!"), on_dismiss=lambda e: print("Dialog dismissed!")
        )

        def close_dlg(e):
            dlg_modal.open = False
            page.update()

        dlg_modal = ft.AlertDialog(
            modal=True,
            title=ft.Text("Please confirm"),
            content=ft.Text("Do you really want to delete all those files?"),
            actions=[
                ft.TextButton("Yes", on_click=close_dlg),
                ft.TextButton("No", on_click=close_dlg),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
            on_dismiss=lambda e: print("Modal dialog dismissed!"),
        )

        def open_dlg(e):
            page.dialog = dlg
            dlg.open = True
            page.update()

        def open_dlg_modal(e):
            page.dialog = dlg_modal
            dlg_modal.open = True
            page.update()

        page.add(
            ft.ElevatedButton("Open dialog", on_click=open_dlg),
            ft.ElevatedButton("Open modal dialog", on_click=open_dlg_modal),
        )

    def confirmar_pedido(e):
        print("Confirmando pedido")
        page.clean()
        
        page.add(
            ft.AppBar(
                title=ft.Text('Comger APP' , size=20),
                bgcolor="blue",
                leading=ft.IconButton(icon="menu"),
                actions=[
                toggledarklight,
                ft.ElevatedButton("Cardápio (Grupos)", 
                    on_click=load_data),
                ]
            ),
        )   
        page.Bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.BLUE,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
            controls=[
                ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                ft.Container(expand=True),
                ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
            ]
            ),
        )         
    def button_clicked(e):
        pass
        
        
    def saida_agrupro(e):
        dicionario = e.control.data
        print(e.control.data)
        print(dicionario['id'],dicionario['a_codigo'])
        
        selectbd
# *******************************************************************************************************************************

    def selectbd_adicadic(e):
        
        page.clean()
        
        if int(txt_number2.value) == 0:
            txt_number2.value = str(int(txt_number2.value) + 1)
        
        
        dicionario2 = e.control.data
        #print(e.control.data)
        #print(dicionario2['pro_cod'],dicionario2['pro_index'])
        txt_pedido2 = (e.control.data['c_descri'])
        #print(txt_pedido)
        
        
        mydt_adic  = ft.DataTable(
            width=540,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            #sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=40,
            data_row_color={"hovered": "0x30FF0000"},
            
            #show_checkbox_column=True,
            #divider_thickness=0,
            column_spacing=5,
                     
            columns=[
                ft.DataColumn(ft.Text('Descrição')),
                ft.DataColumn(ft.Text('Preço')),
                ft.DataColumn(ft.Text('Sel.')),
                ft.DataColumn(ft.Text('Editar')),
            ]
        )    
        
        page.add(
            ft.AppBar(
                    title=ft.Text('Comger APP' , size=20),
                    bgcolor="blue",
                    leading=ft.IconButton(icon="menu"),
                    
                    actions=[
                        toggledarklight,
                        ft.ElevatedButton("Grupos", 
                            on_click=load_data),
                    
                ]
            ),
        )
        
        page.add(
            ft.BottomAppBar(
                bgcolor=ft.colors.BLUE_200,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                controls=[
                    ft.TextField(label="Observações",width=220, height=80),
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number2,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ft.ElevatedButton("Incluir No Pedido", on_click=load_data),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.ADD_CARD_ROUNDED, icon_color=ft.colors.WHITE ,on_click=confirmar_pedido),
                    ft.IconButton(
                        icon=ft.icons.DELETE_FOREVER_ROUNDED,
                        icon_color="pink200",
                        icon_size=40,
                        tooltip="Descartar Pedido",
                    ),
            ]
            ),
        ))
                 
        
        rows = []      
        results = ""
        columns = []
        
        
        page.add(ft.Text(txt_pedido, font_family="Artial" , size=20))
        
        
        
        cursor = mydb.cursor()
        valorx = (e.control.data['pro_index'])
        ncomp = (e.control.data['company_id'])
        ativo ='A'
        #csel   = f'SELECT * FROM produtos where pro_cod = "{valorx}"'
        csel1   = f'SELECT * FROM adic where c_codagru = "{valorx}" and company_id = "{ncomp}"  order by c_descr '
        cursor.execute(csel1)
        results=cursor.fetchall()
        
        columns=[column[0] for column in cursor.description]
        rows=[dict(zip(columns,row)) for row in results]
        cursor.close()        
        if page.txt_gruagru == 2:
            print("2")
            for row in rows:
                mydt_adic.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['c_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['c_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    ft.DataCell(ft.Row([
                                ft.Checkbox(value=False,width=40,height=60),
                    ])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_agrupro),
                    ])),
                    ]
                    )
                    )
           
        if page.txt_gruagru == 1:    
            print("1")
            for row in rows:
                mydt_adic.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['c_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['c_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    ft.DataCell(ft.Row([
                                ft.Checkbox(value=False,width=40,height=60),
                    ])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_agrupro),
                    ])),                    
                    
                    ]
                    )
                    )
                
        page.add(ft.Column([mydt_adic],expand=True, opacity=2))
        
        
        
        

        page.update()        
            
# ************************************************************************************************************************************        
    def selectbd_adic(e):
        
        page.clean()
        
        if int(txt_number2.value) == 0:
            txt_number2.value = str(int(txt_number2.value) + 1)
        
        
        dicionario2 = e.control.data
        #print(e.control.data)
        #print(dicionario2['pro_cod'],dicionario2['pro_index'])
        txt_pedido = (e.control.data['pro_descr'])
        #print(txt_pedido)
        
        
        mydt_adic  = ft.DataTable(
            width=540,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            #sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=40,
            data_row_color={"hovered": "0x30FF0000"},
            
            #show_checkbox_column=True,
            #divider_thickness=0,
            column_spacing=5,
                     
            columns=[
                ft.DataColumn(ft.Text('Descrição')),
                ft.DataColumn(ft.Text('Preço')),
                ft.DataColumn(ft.Text('Sel.')),
                ft.DataColumn(ft.Text('Editar')),
            ]
        )    
        
        page.add(
            ft.AppBar(
                    title=ft.Text('Comger APP' , size=20),
                    bgcolor="blue",
                    leading=ft.IconButton(icon="menu"),
                    
                    actions=[
                        toggledarklight,
                        ft.ElevatedButton("Grupos", 
                            on_click=load_data),
                    
                ]
            ),
        )
        
        page.add(
            ft.BottomAppBar(
                bgcolor=ft.colors.BLUE_200,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                controls=[
                    ft.TextField(label="Observações",width=220, height=80),
                    ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                    txt_number2,
                    ft.IconButton(ft.icons.ADD, on_click=plus_click),
                    ft.ElevatedButton("Incluir No Pedido", on_click=load_data),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.ADD_CARD_ROUNDED, icon_color=ft.colors.WHITE ,on_click=confirmar_pedido),
                    ft.IconButton(
                        icon=ft.icons.DELETE_FOREVER_ROUNDED,
                        icon_color="pink200",
                        icon_size=40,
                        tooltip="Descartar Pedido",
                    ),
            ]
            ),
        ))
                 
        
        rows = []      
        results = ""
        columns = []
        
        
        page.add(ft.Text(txt_pedido, font_family="Artial" , size=20))
        
        
        
        cursor = mydb.cursor()
        valorx = (e.control.data['pro_index'])
        ncomp = (e.control.data['company_id'])
        ativo ='A'
        #csel   = f'SELECT * FROM produtos where pro_cod = "{valorx}"'
        csel1   = f'SELECT * FROM adic where c_codagru = "{valorx}" and company_id = "{ncomp}"  order by c_descr '
        cursor.execute(csel1)
        results=cursor.fetchall()
        
        columns=[column[0] for column in cursor.description]
        rows=[dict(zip(columns,row)) for row in results]
        cursor.close()        
        if page.txt_gruagru == 2:
            print("2")
            for row in rows:
                mydt_adic.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['c_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['c_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    ft.DataCell(ft.Row([
                                ft.Checkbox(value=False,width=40,height=60),
                    ])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_adicadic),
                    ])),
                    ]
                    )
                    )
           
        if page.txt_gruagru == 1:    
            print("1")
            for row in rows:
                mydt_adic.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['c_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['c_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    ft.DataCell(ft.Row([
                                ft.Checkbox(value=False,width=40,height=60),
                    ])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_agrupro),
                    ])),                    
                    
                    ]
                    )
                    )
                
        page.add(ft.Column([mydt_adic],expand=True, opacity=2))
        
        
        
        

        page.update()
                         
# **********************************************************************************************************************************        
    def selectbd(e):
        
        page.clean()
        
        dicionario = e.control.data
        #print(dicionario['id'],dicionario['a_codigo'])
        
        page.txt_gruagru = dicionario['a_grupoagru']

        mydt_produtos = ft.DataTable(
            width=540,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            #sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=40,
            data_row_color={"hovered": "0x30FF0000"},
            
            #show_checkbox_column=True,
            #divider_thickness=0,
            column_spacing=5,
                     
            columns=[
                ft.DataColumn(ft.Text('Descrição')),
                ft.DataColumn(ft.Text('Preço')),
                #ft.DataColumn(ft.Text('Sel.')),
                ft.DataColumn(ft.Text('Editar')),
            ]
        )    
        
        page.add(
            ft.AppBar(
                    title=ft.Text('Comger APP' , size=20),
                    bgcolor="blue",
                    leading=ft.IconButton(icon="menu"),
                    
                    actions=[
                        toggledarklight,
                        ft.ElevatedButton("Grupos", 
                            on_click=load_data),
                ]
            ),
        )
        
        page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.BLUE_200,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
            controls=[
                    #ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.ADD_CARD_ROUNDED, icon_color=ft.colors.WHITE ,on_click=confirmar_pedido),
                    ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color="pink200",
                    icon_size=40,
                    tooltip="Descartar Pedido",
                ),
            ]
            ),
        )  
        rows = []      
        results = ""
        columns = []
        
        cursor = mydb.cursor()
        valorx = (e.control.data['a_codigo'])
        ncomp  = (e.control.data['company_id'])
        ativo  ='A'
        #csel   = f'SELECT * FROM produtos where pro_cod = "{valorx}"'
        csel1   = f'SELECT * FROM produtos where pro_index = "{valorx}" and company_id = "{ncomp}" and pro_ad = "{ativo}" order by pro_descr '
        cursor.execute(csel1)
        results=cursor.fetchall()
        
        columns=[column[0] for column in cursor.description]
        rows=[dict(zip(columns,row)) for row in results]
        cursor.close()        
        for row in rows:
                mydt_produtos.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['pro_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['pro_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    
                    #    ft.DataCell(ft.Row([
                    #        ft.Checkbox(value=False,width=40,height=60),
                    #    ])),
                    
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_adic),
                    ])),
                    ]
                    )
                    )
        page.add(ft.Column([mydt_produtos],expand=True, opacity=2))
        page.update()
 
 # **********************************************************************************************************************************        
    def selectbd_agrupro(e):
        
        page.clean()
        
        dicionario3 = e.control.data
        #print(e.control.data)
        #print(dicionario3['c_codagru'],dicionario3['company_id'])

        mydt_produtos = ft.DataTable(
            width=540,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            #sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=40,
            data_row_color={"hovered": "0x30FF0000"},
            
            #show_checkbox_column=True,
            #divider_thickness=0,
            column_spacing=5,
                     
            columns=[
                ft.DataColumn(ft.Text('Descrição')),
                ft.DataColumn(ft.Text('Preço')),
                ft.DataColumn(ft.Text('Sel.')),
                ft.DataColumn(ft.Text('Editar')),
            ]
        )    
        
        page.add(
            ft.AppBar(
                    title=ft.Text('Comger APP' , size=20),
                    bgcolor="blue",
                    leading=ft.IconButton(icon="menu"),
                    
                    actions=[
                        toggledarklight,
                        ft.ElevatedButton("Grupos", 
                            on_click=load_data),
                ]
            ),
        )
        
        page.bottom_appbar = ft.BottomAppBar(
            bgcolor=ft.colors.BLUE_100,
            shape=ft.NotchShape.CIRCULAR,
            content=ft.Row(
            controls=[
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.ADD_CARD_ROUNDED, icon_color=ft.colors.WHITE ,on_click=confirmar_pedido),
                    ft.IconButton(
                    icon=ft.icons.DELETE_FOREVER_ROUNDED,
                    icon_color="pink200",
                    icon_size=40,
                    tooltip="Descartar Pedido",
                ),
            ]
            ),
        )  
        rows = []      
        results = ""
        columns = []
        
        cursor = mydb.cursor()
        valorx = (e.control.data['c_codagru'])
        ncomp  = (e.control.data['company_id'])
        ativo  ='A'
        #csel   = f'SELECT * FROM produtos where pro_cod = "{valorx}"'
        csel1   = f'SELECT * FROM produtos where pro_index = "{valorx}" and company_id = "{ncomp}" and pro_ad = "{ativo}" order by pro_descr '
        cursor.execute(csel1)
        results=cursor.fetchall()
        
        columns=[column[0] for column in cursor.description]
        rows=[dict(zip(columns,row)) for row in results]
        cursor.close()        
        for row in rows:
                mydt_produtos.rows.append(
                ft.DataRow(
                    selected=True,
                    cells=[
                    ft.DataCell(ft.Text(row['pro_descr'], width=120, height=60,size=11,weight=ft.FontWeight.W_600)),
                    ft.DataCell(ft.Text(row['pro_venda'], width=40, height=80,weight=ft.FontWeight.W_800)),
                    ft.DataCell(ft.Row([
                        ft.Checkbox(value=False,width=40,height=60),
                    ])),
                    ft.DataCell(ft.Row([
                        ft.IconButton(icon='create',
                        icon_color='blue',
                        data=row,
                        width= 40,
                        height=60,
                        icon_size=20,
                        bgcolor=ft.colors.WHITE70,
                        selected_icon_color="blue",
                        on_click=selectbd_adic),
                    ])),
                    ]
                    )
                    )
        page.add(ft.Column([mydt_produtos],expand=True, opacity=2))
        
        ctn= ft.Container(
                gradient=ft.RadialGradient(
                colors=[ft.colors.YELLOW, ft.colors.BLUE],
                ),
                width=150,
                height=150,
                border_radius=5,
            )
        page.add(ctn)
                
        page.update()                
    
    
    def grupo_sel(e):
        pass
        #print("grupo sel")    
# ********************************************************************************************************************************        
    # FINAL PROIDUTOS PERTENCENTES AO AGRUPAMENTO    
    # AGRUPAMENTOS ( GRUPOS )    
    def load_data(e):
        #print("load_data")
        #print(e.control.data.value)
        page.clean()
        
        mydt = ft.DataTable(
            width=540,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(2, "black"),
            border_radius=10,
            vertical_lines=ft.border.BorderSide(1, "black"),
            horizontal_lines=ft.border.BorderSide(1, "black"),
            #sort_column_index=0,
            sort_ascending=True,
            heading_row_color=ft.colors.BLACK12,
            heading_row_height=40,
            data_row_color={"hovered": "0x30FF0000"},
            
            #show_checkbox_column=True,
            #divider_thickness=0,
            column_spacing=5,
            columns=[
                #ft.DataColumn(ft.Text('Cod')),
                ft.DataColumn(ft.Text('Cardápio')),
                ft.DataColumn(ft.Text('Selecionar')),
            ]
        )    
        page.add(
            ft.AppBar(
                title=ft.Text('Comger APP' , size=20),
                bgcolor="blue",
                leading=ft.IconButton(icon="menu"),
                actions=[
                toggledarklight
                ]
            ),
        )
        page.add(
                ft.BottomAppBar(
                bgcolor=ft.colors.BLUE,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
                ),
        )
    )     
        
        cursor = mydb.cursor()
        ncompa = 1
        csel  = f'SELECT * FROM agrupro where company_id = "{ncompa}" order by a_descr '
        cursor.execute(csel)
        results=cursor.fetchall()
         
        columns=[column[0] for column in cursor.description]
        rows=[dict(zip(columns,row)) for row in results]
        
        for row in rows:
                mydt.rows.append(
                    ft.DataRow(
                        cells=[
                            #ft.DataCell(ft.Text(row['a_codigo'], width=30 , height=80,size=12)),
                            ft.DataCell(ft.Text(row['a_descr'], width=180 , height=80,size=16)),
                            ft.DataCell(ft.Row([
                                ft.IconButton(icon='add',
                                    icon_color='blue',
                                    data=row,
                                    on_click=selectbd,
                                    aspect_ratio=1,
                                    
                                    width= 60,
                                    height=60,
                                    icon_size=20,
                                    selected_icon_color="red",),
                                ])),
                            ],  
                    on_select_changed=grupo_sel         
                )
            )
        page.add(ft.Column([mydt]))
        page.update() 
        
        
    #print("menu_inicio")
    page.add(
                ft.AppBar(
                    title=ft.Text('Comger APP' , size=20),
                    bgcolor="blue",
                    leading=ft.IconButton(icon="menu"),
                    actions=[
                    toggledarklight,
                    ft.ElevatedButton("Cardápio (Grupos)", 
                        on_click=load_data),
                    ]
                ),
        )   
    #page.Bottom_appbar = ft.BottomAppBar(
    page.add(
                ft.BottomAppBar(
                bgcolor=ft.colors.BLUE,
                shape=ft.NotchShape.CIRCULAR,
                content=ft.Row(
                controls=[
                    ft.IconButton(icon=ft.icons.MENU, icon_color=ft.colors.WHITE),
                    ft.Container(expand=True),
                    ft.IconButton(icon=ft.icons.SEARCH, icon_color=ft.colors.WHITE),
                    ft.IconButton(icon=ft.icons.FAVORITE, icon_color=ft.colors.WHITE),
                ]
                ),
        )
    )     
        
            
    #load_data()
 ##   def addtodb(e):
 ##   load_data()
 ##
 ##   load_data()
        
    # mydb.commit()
    # mydb.close()
    
    page.add()
    
    #mydb.commit()
    #mydb.close()
    
        
    page.update()
ft.app(target=main, assets_dir="assets")
#ft.app(target=main, view=ft.AppView.WEB_BROWSER)    