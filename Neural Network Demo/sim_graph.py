from graphics import GraphicsWindow
def simulate_drop_graph(m,x,y,z,vx,vy,vz,dx,dy,dz,wx,wy,wz,step = 0.01):

    wintop = GraphicsWindow(800,600)
    winside = GraphicsWindow(800,600)
    winfront = GraphicsWindow(800,600)

    plottop = wintop.canvas()
    plotside = winside.canvas()
    plotfront = winfront.canvas()

    xstart = 400
    ystart = 300
    zstart = 100

    xlabel = ylabel = 100
    zground = 500

    plottop.setOutline("white")
    plottop.setBackground("black")
    plottop.drawText(xlabel,ylabel,"top view")
    plotside.setOutline("white")
    plotside.setBackground("black")
    plotside.drawText(xlabel,ylabel,"side view")
    plotfront.setOutline("white")
    plotfront.setBackground("black")
    plotfront.drawText(xlabel,ylabel,"front view")

    plotside.drawLine(0,zground,800,zground)
    plotside.drawText(100,zground,"ground")
    plotfront.drawLine(0,zground,800,zground)
    plotfront.drawText(100,zground,"ground")

    t = 0
    g = 9.81
    while z > 0:
        t += step
        fx = dx * (vx - wx)**2
        fy = dy * (vy - wy)**2
        fz = dz * (vz - wz)**2 - g

        ax = fx / m
        ay = fy / m
        az = fz / m

        x += vx * step + 0.5 * ax * step**2
        y += vy * step + 0.5 * ay * step**2
        z += vz * step + 0.5 * az * step**2

        vx += ax * step
        vy += ay * step
        vz += az * step

        plottop.drawPoint(xstart+5*x,ystart+5*y)
        plotside.drawPoint(xstart+5*x,500-5*z)
        plotfront.drawPoint(ystart+5*y,500-5*z)

    wintop.wait()
    winside.wait()
    winfront.wait()

    return (t,x,y,z)
