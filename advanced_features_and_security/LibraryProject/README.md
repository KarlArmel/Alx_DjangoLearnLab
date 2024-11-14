# Permissions and Groups Setup

This Django project includes custom permissions and groups to manage access to `Book` objects.

## Permissions:
- `can_view`: Allows users to view book instances.
- `can_create`: Allows users to create new book instances.
- `can_edit`: Allows users to edit existing book instances.
- `can_delete`: Allows users to delete book instances.

## Groups:
- **Viewers**: Users in this group can view books (`can_view`).
- **Editors**: Users in this group can create and edit books (`can_create`, `can_edit`).
- **Admins**: Users in this group have all permissions (`can_view`, `can_create`, `can_edit`, `can_delete`).
