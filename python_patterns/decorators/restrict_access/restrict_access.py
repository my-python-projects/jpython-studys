import logging
from functools import wraps

logging.basicConfig(
    filename="access_denied.log",
    level=logging.WARNING,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

def restrict_access(required_permissions, error_message=None, log_on_deny=True):
    if error_message is None:
        error_message = "Acesso negado: permissões insuficientes"

    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            user_permissions = set(user.get("permissions", []))
            required = set(required_permissions)

            if required.issubset(user_permissions):
                return func(user, *args, **kwargs)
            else:
                print(error_message)
                if log_on_deny:
                    logging.warning(
                        f"Acesso negado à função '{func.__name__}' para usuário '{user.get('name', 'Unknown')}'"
                    )
        return wrapper
    return decorator


@restrict_access(["admin", "write"], error_message="Você não tem permissão para excluir usuários!")
def delete_user(user, user_id):
    print(f"Usuário {user_id} deletado por {user['name']}")


if __name__ == '__main__':

    user = {"name": "Alice", "permissions": ["admin", "write"]}
    delete_user(user, 123)  # Deve executar

    user_no_perm = {"name": "Bob", "permissions": ["read"]}
    delete_user(user_no_perm, 123)  # Deve falhar


