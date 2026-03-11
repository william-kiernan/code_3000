import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    """
    Attempt to link anonymized records to auxiliary records
    using exact matching on quasi-identifiers.

    Returns a DataFrame with columns:
      anon_id, matched_name
    containing ONLY uniquely matched records.
    """
    # Columns that should not be used for matching
    excluded_cols = {"anon_id", "name", "matched_name"}

    # Use shared columns as quasi-identifiers
    match_cols = [
        col for col in anon_df.columns
        if col in aux_df.columns and col not in excluded_cols
    ]

    # Merge anonymized and auxiliary data on quasi-identifiers
    merged = anon_df.merge(aux_df, on=match_cols, how="inner")

    # Keep only anon_id values that map to exactly one auxiliary record
    unique_matches = merged.groupby("anon_id").filter(lambda g: len(g) == 1)

    # Return only the required columns
    return unique_matches[["anon_id", "name"]].rename(
        columns={"name": "matched_name"}
    )


def deanonymization_rate(matches_df, anon_df):
    """
    Compute the fraction of anonymized records
    that were uniquely re-identified.
    """
    if len(anon_df) == 0:
        return 0.0
    return len(matches_df) / len(anon_df)
