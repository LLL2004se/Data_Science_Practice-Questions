def analyze_events(batches: list) -> tuple:
    if not batches:
        return ([], set(), set(), 0)

    # Store unique IDs in first-seen order
    unique_ids = []
    seen = set()

    for batch in batches:
        for event_id in batch:
            if event_id not in seen:
                seen.add(event_id)
                unique_ids.append(event_id)

    # Convert each batch to a set to remove duplicates
    batch_sets = [set(batch) for batch in batches]

    # IDs appearing in every batch
    common_ids = batch_sets[0].intersection(*batch_sets[1:])

    # All distinct IDs across every batch
    all_ids = {event_id for batch in batches for event_id in batch}

    # IDs that are not common to every batch
    non_common_ids = all_ids - common_ids

    unique_count = len(all_ids)

    return (unique_ids, common_ids, non_common_ids, unique_count)
