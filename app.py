from shiny import App, module, reactive, render, ui
from obsbot import open_dev, write_ai_mode
import usb1

@module.ui
def button_ui(text):
    return ui.input_action_button("mode", text)

@module.server
def button_server(input, output, session, mode):
    @reactive.effect
    @reactive.event(input.mode)
    async def _():
        dev.claimInterface(0)
        dev.resetDevice()
        write_ai_mode(dev, mode)
        dev.releaseInterface(0)

vid_want = 0x3564
pid_want = 0xFEF8

usbcontext = usb1.USBContext()
dev = open_dev(vid_want, pid_want, usbcontext)
dev.setAutoDetachKernelDriver(True)

app_ui = ui.page_fluid(
    ui.tags.style("""
    body { 
      --bs-body-bg: #2B2E38;
    }
    
    button.btn.action-button {
      width: 8em;
      margin-top: 0.25em;
      --bs-btn-bg: #3C404B;
      --bs-btn-hover-bg: #4F535E;
      --bs-btn-color: #FEFEFE;
      --bs-btn-padding-x: 1em;
      --bs-btn-padding-y: 0.25em;
      --bs-btn-font-size: 0.8rem;
    }
    """),
    button_ui("stop", "Stop"),
    button_ui("normal", "Normal"),
    button_ui("upperbody", "Upper-body"),
    button_ui("closeup", "Close-up"),
    button_ui("headless", "Headless"),
    button_ui("lowerbody", "Lower-body"),
    button_ui("desk", "Desk"),
    button_ui("whiteboard", "Whiteboard"),
    button_ui("hand", "Hand"),
    button_ui("group", "Group")
)

def server(input, output, session):
    [button_server(x, mode = x) for x in ['stop', 'normal', 'upperbody', 'closeup', 'headless', 'lowerbody', 'desk', 'whiteboard', 'hand', 'group']]

app = App(app_ui, server)
