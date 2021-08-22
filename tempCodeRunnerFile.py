    df = pd.DataFrame.from_dict(a, orient='index')
    df = df.transpose()
    df.to_csv(r'Report.csv')
    print(df)
