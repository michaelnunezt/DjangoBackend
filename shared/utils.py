from math import ceil


def paginate_queryset(queryset, page, per_page):
    """
    Paginates a queryset.
    :param queryset: Queryset to paginate
    :param page: Current page number (1-indexed)
    :param per_page: Number of items per page
    :return: Paginated queryset, total pages, per page count
    """
    total_items = queryset.count()
    total_pages = ceil(total_items / per_page)
    start = (page - 1) * per_page
    end = start + per_page
    return queryset[start:end], total_pages, per_page
