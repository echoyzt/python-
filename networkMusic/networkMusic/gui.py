from tkinter import *
from tkinter import ttk
from io import BytesIO
from mutagen.mp3 import MP3
from PIL import Image, ImageTk
import get
import player
import lrc

class Window(Tk):
    ischanging = False
    last_pos = 0

    words = ['']
    times = [0]
    
    def __init__(self):

        Tk.__init__(self)
        self.title('JIE 音乐')
        self.geometry('650x400')
        self.resizable(0, 0)

        self.set_notebook()
        self.set_control()

        self.set_weight()

        self.update()

        self.after(100, self.timer)

        self.mainloop()

    def set_notebook(self):
        self.nb = ttk.Notebook(self)
        self.nb.grid(row=0, column=0, sticky='nswe', padx=2, pady=1)

        self.set_search_frame()
        self.set_lrc_frame()

        self.nb.add(self.search_frame, text=' 搜索 ')
        self.nb.add(self.lrc_frame, text=' 歌词 ')

    # 控制框
    def set_control(self):
        self.control_frame = Frame(self)
        self.control_frame.grid(row=1, column=0, sticky='nswe', padx=2, pady=1)

        self.ctrl_pic = Canvas(self.control_frame, height=40, width=40)
        self.ctrl_pic.grid(row=0, column=0)

        self.play_btn = Label(self.control_frame, text='▶', font=('宋体', 24, 'bold'), 
                              width=2, height=1, relief='flat')
        self.play_btn.bind('<Enter>', lambda event: self.play_btn.configure(fg='orange'))
        self.play_btn.bind('<Leave>', lambda event: self.play_btn.configure(fg='black'))
        self.play_btn.bind('<Button-1>', self.play_or_pause)
        self.play_btn.grid(row=0, column=1, sticky='nswe')

        self.var = IntVar()
        self.var.set(0)

        self.bar = Scale(self.control_frame, label='无歌曲', orient='horizontal', 
                         variable=self.var, showvalue=False, from_=0, to=0, 
                         command=self.change, width=10, length=500)
        self.bar.grid(row=0, column=2, sticky='nwe')

        self.download_btn = Label(self.control_frame, text='↓', font=('微软雅黑', 15), width=2)
        self.download_btn.bind('<Enter>', lambda event: self.download_btn.configure(fg='orange'))
        self.download_btn.bind('<Leave>', lambda event: self.download_btn.configure(fg='black'))
        self.download_btn.bind('<Button-1>', self.download)
        self.download_btn.grid(row=0, column=3, sticky='nswe')

    # 搜索界面
    def set_search_frame(self):
        self.search_frame = Frame(self.nb)

        self.inputbox = ttk.Entry(self.search_frame, width=14)
        self.inputbox.bind('<Return>',lambda event: self.get_datas(self.inputbox.get()))
        self.inputbox.grid(row=0, column=0, sticky='nswe', padx=(2, 0), pady=2)

        self.surebtn = ttk.Button(self.search_frame, text='搜索', width=6, 
                                  command=lambda: self.get_datas(self.inputbox.get()))
        self.surebtn.grid(row=0, column=1, columnspan=2, sticky='nswe', padx=(0, 2), pady=2)
        
        columns = [0, 1, 2, 3, 4]
        self.songstable = ttk.Treeview(self.search_frame, columns=columns, show='headings')
        
        self.songstable.column(0, width=25, anchor='w', stretch='no')
        self.songstable.heading(0, text='')
        self.songstable.column(1, width=200, anchor='w')
        self.songstable.heading(1, text='歌曲')
        self.songstable.column(2, width=70, anchor='w')
        self.songstable.heading(2, text='歌手')
        self.songstable.column(3, width=100, anchor='w')
        self.songstable.heading(3, text='专辑')
        self.songstable.column(4, width=45, anchor='w', stretch='no')
        self.songstable.heading(4, text='时长')

        self.songstable.grid(row=1, column=0, columnspan=2, sticky='nswe')
        self.songstable.bind('<Double-Button-1>', 
                             lambda event: self.selected(self.songstable.item(self.songstable.selection()[0], 'value')))

        self.songscroll = ttk.Scrollbar(self.search_frame, orient='vertical', 
                                        command=self.songstable.yview)
        self.songscroll.grid(row=1, column=2, sticky='nswe')

        self.songstable.configure(yscrollcommand=self.songscroll.set)

    # 歌词界面
    def set_lrc_frame(self):
        self.lrc_frame = Frame(self.nb)

        self.lrc_title = Label(self.lrc_frame, text='无歌曲', font=('微软雅黑', 15), anchor='w')
        self.lrc_title.grid(row=0, column=1, sticky='nswe', padx=(0, 40), pady=(40, 0))
        self.lrc_title2 = Label(self.lrc_frame, text='佚名', font=('微软雅黑', 10), fg='grey', anchor='w')
        self.lrc_title2.grid(row=1, column=1, sticky='nswe', padx=(0, 40))

        self.lrc_list = Listbox(self.lrc_frame, relief='flat', font=('微软雅黑', 12), 
                                highlightthickness=0, selectmode='single',
                                bg='SystemButtonFace', fg='#303030',
                                selectbackground='SystemButtonFace', selectforeground='orange')
        self.lrc_list.grid(row=2, column=1, sticky='nswe', padx=(0, 40), pady=(10, 40))
        self.lrc_list.insert('end', *([''] * 3), '无歌词')

        self.lrc_pic = Canvas(self.lrc_frame, width=240, height=240, relief='flat')
        self.lrc_pic.grid(row=0, column=0, rowspan=3, padx=40, pady=40)

    def set_weight(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.search_frame.grid_rowconfigure(1, weight=1)
        self.search_frame.grid_columnconfigure(0, weight=1)

        self.lrc_frame.grid_rowconfigure(2, weight=1)
        self.lrc_frame.grid_columnconfigure(1, weight=1)

    # 搜索
    def get_datas(self, kw='str'):
        t = self.songstable.get_children()
        for item in t:
            self.songstable.delete(item)

        datas = kuwo.search_kuwo(kw)

        for index, value in enumerate(datas):
            self.songstable.insert('','end',value=[index+1, *value])

    # 选中歌曲
    def selected(self, datas):
        player.reset()

        self.mdatas = datas
        self.last_pos = 0
        self.index = 0

        self.lrc = lrcdecoder.decode(kuwo.get_music_lrc(datas[-1]))
        self.words = lrcdecoder.Words
        self.times = lrcdecoder.Times

        self.content = kuwo.get_music_content(datas[-1])
        self.song_name = datas[1]
        self.song_artist = datas[2]

        self.pic_small = self.Tkpic(kuwo.get_pic(datas[-2]), 40)
        self.pic_large = self.Tkpic(kuwo.get_pic(datas[-3]), 240)

        self.ctrl_pic.create_image(0, 0, anchor='nw', image=self.pic_small)
        self.lrc_pic.create_image(0, 0, anchor='nw', image=self.pic_large)

        self.play_btn.configure(text='||')

        self.lrc_title.configure(text=self.song_name)
        self.lrc_title2.configure(text=self.song_artist)
     
        self.lrc_list.delete(0, 'end')
        self.lrc_list.insert('end', *[*([''] * 2), *self.words])

        byte = BytesIO(self.content)

        self.bar.configure(from_=0, to=MP3(byte).info.length, label=f'{datas[1]} - {datas[2]}')
        player.load(byte)
        player.play()

    # 将网络 png 图片用于 tkinter 中
    def Tkpic(self, pic, res):
        byte_obj = BytesIO(pic)

        pic = Image.open(byte_obj)
        pic = pic.resize((res, res), Image.ANTIALIAS)
        pic = ImageTk.PhotoImage(pic)

        return pic

    # 拖动进度条时
    def change(self, value):
        self.ischanging = True

    # 暂停、继续
    def play_or_pause(self, event):
        if self.play_btn['text'] == '||' :
            player.pause()
            self.play_btn.configure(text='▶')
        else:
            player.unpause()
            self.play_btn.configure(text='||')

    # 下载音乐
    def download(self, event):
        with open(f'musics/{self.song_name} - {self.song_artist}.mp3', 'wb+') as f:
            f.write(self.content)

    # 定时器
    def timer(self):
        # 歌词同步
        if self.ischanging:
            self.ischanging = False
            self.last_pos = self.var.get() - player.get_pos() / 1000
            player.set_pos(self.var.get())
        else:
            self.var.set(player.get_pos() / 1000 + self.last_pos)

        # 歌词高亮
        index = lrcdecoder.get_index(player.get_pos() / 1000 + self.last_pos)
        self.lrc_list.selection_clear(0, 'end')
        self.lrc_list.selection_set(index + 2)

        # 滚动到指定位置
        index = index / len(self.words)
        index = index if index >= 0 else 0

        self.lrc_list.yview_moveto(index)

        self.after(200, self.timer)

kuwo = get.Kuwo()
player = player.Player()
lrcdecoder = lrc.Lrc()