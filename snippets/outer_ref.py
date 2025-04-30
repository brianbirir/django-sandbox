"""
In Django, OuterRef enables subqueries to reference fields from the outer query. 
It is typically used within Subquery expressions, allowing filtering or annotation based on related data. 
OuterRef makes it possible to correlate data between the main query and its subquery, which is useful 
in complex database operations. The behavior of OuterRef depends on the context where the query is used, 
often involving Exists or limit 1 to handle single or subset results.


In the examples below, OuterRef('pk') references the primary key of the Author model in the outer query,
allowing the subquery to 
filter or check for related Book objects.
"""


from django.db.models import OuterRef, Subquery, Exists
from myapp.models import Author, Book

# Example: Annotating authors with the existence of a book
Author.objects.annotate(
    has_book=Exists(Book.objects.filter(author_id=OuterRef('pk')))
)

# Example: Filtering authors who have written a book
Author.objects.filter(
    books__in=Subquery(Book.objects.filter(author_id=OuterRef('pk')).values('pk')[:1])
)
