def get_top_schools(df, top_n=10):
    top_schools = df.nlargest(top_n, 'average_math')[['school_name', 'average_math']]
    return top_schools