aqi_tbl = [
    [0, 'great'],
    [26, 'good'],
    [51, 'moderate'],
    [101, 'unhealthy'],
    [201, 'very unhealthy']
]

def vlookup(v, tbl, col):
    r = max(filter(lambda n: v >= n[0], tbl))
    return r[col]

if __name__ == "__main__":
    aqi = 101
    print(vlookup(aqi, aqi_tbl,1))