# dashApi/core/plotter.py
import io
from plotnine import ggplot, aes, geom_point, scale_x_log10, labs, theme_minimal
from gapminder import gapminder


def generate_gapminder_plot_bytes(year: int) -> bytes:
    df_year = gapminder[gapminder["year"] == year]
    if df_year.empty:
        raise ValueError(f"No data found for year {year}")

    p = (
        ggplot(df_year, aes("gdpPercap", "lifeExp", size="pop", color="continent"))
        + geom_point(alpha=0.6)
        + scale_x_log10()
        + labs(
            title=f"Gapminder Data for {year}",
            x="GDP per Capita (log scale)",
            y="Life Expectancy",
        )
        + theme_minimal()
    )

    fig = p.draw()

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    buf.seek(0)
    return buf.getvalue()
