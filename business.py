from escpos.printer import Serial

DEVICE = '/dev/ttyS4'

p = Serial(DEVICE, baudrate=115200)

p.set(align='center', double_width=True, double_height=True)

p.image('logo.bmp')

p.ln()

p.textln('Robert Kossessa')

p.ln()

p.set(align='center', double_width=False, double_height=False)

p.block_text('I\'m a Computer Science student at Karlsruhe Institute of Technology, interested in informatics, games, music and art. I love programming, playing the piano and helping less experienced computer users.', columns=30)


p.ln(2)

p.textln('Check out my website:')

p.ln()

p.set(align='center', double_width=True, double_height=True)

p.text('KOSRO.DE')

p.qr('https://Kosro.de', size=10)

p.cut()
