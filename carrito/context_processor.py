from carrito. carro import Cart


def importe_total(request):
    total = 0.0

    if request.user.is_active or request.user.is_anonymous:

        if 'cart' in request.session:
            cantidadArt = []
            for key, value in request.session['cart'].items():

                cantidadArt.append(value['cantidad'])
                sumando = sum(cantidadArt)


                subtotal = total + \
                    (float(value['precio'])*value['cantidad'])
                total = round(subtotal, 2)

    return {'importe_total': total}
