import numpy as np
import cv2
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

FILE_I_END = 1

data_order = [i for i in range(1, FILE_I_END + 1)]


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Data Approval")
        self.pack(fill=BOTH, expand=1)
        images_1_2_h_rgb = cv2.cvtColor(images_1_2_h, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(images_1_2_h_rgb, 'RGB')
        imgtk = ImageTk.PhotoImage(image=im)
        label = Label(image=imgtk)
        label.image = imgtk
        label.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()
        self.modify_button = Button(self, text="Modify!", command=self.modify)
        self.modify_button.pack()
        self.choice2 = []

    def approve(self):
        approved_data.append([img, choice])
        print("Data point " + str(data) + " was approved!")
        root.destroy()

    def approve_mod(self):
        approved_data.append([img, self.choice2])
        print("Data point " + str(data) + " was modified and approved!")
        root.destroy()

    def exclude(self):
        print("Data point " + str(data) + " will be excluded!")
        root.destroy()

    def modify(self):
        self.approve_button.destroy()
        self.exclude_button.destroy()
        self.modify_button.destroy()
        w_button = Button(self, text="W", command=self.mod_w)
        w_button.pack()
        s_button = Button(self, text="S", command=self.mod_s)
        s_button.pack()
        a_button = Button(self, text="A", command=self.mod_a)
        a_button.pack()
        d_button = Button(self, text="D", command=self.mod_d)
        d_button.pack()
        aw_button = Button(self, text="AW", command=self.mod_aw)
        aw_button.pack()
        dw_button = Button(self, text="DW", command=self.mod_dw)
        dw_button.pack()
        as_button = Button(self, text="AS", command=self.mod_as)
        as_button.pack()
        ds_button = Button(self, text="DS", command=self.mod_ds)
        ds_button.pack()
        nk_button = Button(self, text="NK", command=self.mod_nk)
        nk_button.pack()

    def mod_w(self):
        self.choice2 = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_s(self):
        self.choice2 = [0, 1, 0, 0, 0, 0, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_a(self):
        self.choice2 = [0, 0, 1, 0, 0, 0, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_d(self):
        self.choice2 = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_aw(self):
        self.choice2 = [0, 0, 0, 0, 1, 0, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_dw(self):
        self.choice2 = [0, 0, 0, 0, 0, 1, 0, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_as(self):
        self.choice2 = [0, 0, 0, 0, 0, 0, 1, 0, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_ds(self):
        self.choice2 = [0, 0, 0, 0, 0, 0, 0, 1, 0]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()

    def mod_nk(self):
        self.choice2 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
        message1 = Label(text="Choice changed to: " + str(choice))
        message1.pack()
        message2 = Label(text="Please Approve or Reject this change.")
        message2.pack()
        self.approve_button = Button(self, text="Approve!", command=self.approve_mod)
        self.approve_button.pack()
        self.exclude_button = Button(self, text="Reject!", command=self.exclude)
        self.exclude_button.pack()


try:
    root = Tk()
    file_name = filedialog.askopenfilename(filetypes=[("Numpy Files", "*.npy")])
    root.destroy()
    train_data = np.load(file_name, allow_pickle=True)
    approved_data = []
    for data in train_data:
        img = data[0]
        choice = data[1]
        if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:
            choice_img = 'key_images/w.png'
        elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:
            choice_img = 'key_images/s.png'
        elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:
            choice_img = 'key_images/a.png'
        elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:
            choice_img = 'key_images/d.png'
        elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:
            choice_img = 'key_images/aw.png'
        elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:
            choice_img = 'key_images/dw.png'
        elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:
            choice_img = 'key_images/as.png'
        elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:
            choice_img = 'key_images/ds.png'
        elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:
            choice_img = 'key_images/nk.png'
        else:
            print('no matches')
        img2 = cv2.imread(choice_img)
        img2 = cv2.resize(img2, (250, 270))
        images_1_2_h = np.concatenate((img, img2), axis=1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

        root = Tk()
        root.geometry("+1000+500")
        app = Window(root)
        root.mainloop()
    root = Tk()
    save_file_name = filedialog.asksaveasfilename(filetypes=[("Numpy Files", "*.npy")])
    root.destroy()
    np.save(save_file_name, approved_data)

except Exception as e:
    print(str(e))
