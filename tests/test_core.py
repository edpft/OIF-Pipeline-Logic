# Local
from oiflib.core import melt
from oiflib.testing import are_dfs_equal


def test_actual_equals_expected(spark):
    """Return true if actual DataFrame and expected DataFrame are equal"""

    # Create test input
    input_received = spark.createDataFrame(
        data=[
            ["a", 1, 2],
            ["b", 3, 4],
            ["c", 5, 6],
        ],
        schema=["A", "B", "C"],
    )

    # Create expected output
    output_expected = spark.createDataFrame(
        data=[
            ["a", "B", 1],
            ["b", "B", 3],
            ["c", "B", 5],
            ["a", "C", 2],
            ["b", "C", 4],
            ["c", "C", 6],
        ],
        schema=["A", "variable", "value"],
    )

    # Apply function to input
    output_actual = melt(df=input_received, id_vars="A")

    assert are_dfs_equal(output_expected, output_actual)
