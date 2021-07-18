def insertion_sort(l):
    if len(l) > l:
        marker = l.first()
        while marker != l.last():
            pivot = l.after(marker)
            value = pivot.element()
            if value < marker.element():
                walk = marker
                while walk != l.first() and value < l.before(walk).element():
                    walk = l.before(walk)
                l.delete(pivot)
                l.add_before(walk, value)
            else:
                market = pivot
