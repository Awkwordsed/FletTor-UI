import os
import flet
import requests
import subprocess

def main(page: flet.Page):
    page.title="Pox"
    page.fonts= {
        "pixel": "http://watchdogsfont.com/font/PixelOperatorMono.ttf"
    }
    page.theme=flet.theme.Theme(font_family="pixel")

    page.window.width=300
    page.window.height=400

    page.vertical_alignment="center"
    page.horizontal_alignment="center"

    page.theme_mode="dark"
    page.bgcolor="#000000"

    def torcheck():
        status.value="checking.."
        status.update()

        #os.system("pkill -HUP tor")
        out1=subprocess.run("tor", shell=True)
        print(out1)
        #out1.value=ipaddr
        #out1.update()

        try:

            res = requests.get(
                url="http://checkip.amazonaws.com/",
                proxies={
                    "http": "socks5://127.0.0.1:9050",
                    "https": "socks5://127.0.0.1:9050"
                }
            ).text.split("\n")[0]
            print(res)

            lst = requests.get(
                url="https://www.dan.me.uk/torlist/",
                proxies={
                    "http": "socks5://127.0.0.1:9050",
                    "https": "socks5://127.0.0.1:9050"
                }
            ).text.split("\n")
            print(lst)

            ipaddr.value=res
            ipaddr.color="#00aaff"
            ipaddr.update()

            if res in lst:
                status.value="connected"
                status.update()
            else:
                status.value="disconnected"
                status.update()
        except Exception as e:
            status.value="errorrrrr   lol\n" + str(e)
            status.update()



    page.add(
        flet.TextButton(
            content=flet.Text("Start", size=17, weight="bold"),
            style=flet.ButtonStyle(
                color="#ffffff",
                bgcolor="#000000",
                shape=flet.RoundedRectangleBorder(
                    radius=0
                ),
                side=flet.BorderSide(
                    width=1,
                    color="#ffffff"
                )
            ),
            on_click=lambda _:torcheck()
        ),
        ipaddr:=flet.Text("ip"),
        status:=flet.Text("status = unknown"),
        torout:=flet.Text("")
    )

if __name__ == "__main__":
    flet.app(target=main)
