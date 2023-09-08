from _typeshed import Incomplete

from influxdb_client.service._base_service import _BaseService

class UsersService(_BaseService):
    def __init__(self, api_client: Incomplete | None = None) -> None: ...
    def delete_users_id(self, user_id, **kwargs): ...
    def delete_users_id_with_http_info(self, user_id, **kwargs): ...
    async def delete_users_id_async(self, user_id, **kwargs): ...
    def get_flags(self, **kwargs): ...
    def get_flags_with_http_info(self, **kwargs): ...
    async def get_flags_async(self, **kwargs): ...
    def get_me(self, **kwargs): ...
    def get_me_with_http_info(self, **kwargs): ...
    async def get_me_async(self, **kwargs): ...
    def get_users(self, **kwargs): ...
    def get_users_with_http_info(self, **kwargs): ...
    async def get_users_async(self, **kwargs): ...
    def get_users_id(self, user_id, **kwargs): ...
    def get_users_id_with_http_info(self, user_id, **kwargs): ...
    async def get_users_id_async(self, user_id, **kwargs): ...
    def patch_users_id(self, user_id, user, **kwargs): ...
    def patch_users_id_with_http_info(self, user_id, user, **kwargs): ...
    async def patch_users_id_async(self, user_id, user, **kwargs): ...
    def post_users(self, user, **kwargs): ...
    def post_users_with_http_info(self, user, **kwargs): ...
    async def post_users_async(self, user, **kwargs): ...
    def post_users_id_password(self, user_id, password_reset_body, **kwargs): ...
    def post_users_id_password_with_http_info(self, user_id, password_reset_body, **kwargs): ...
    async def post_users_id_password_async(self, user_id, password_reset_body, **kwargs): ...
    def put_me_password(self, password_reset_body, **kwargs): ...
    def put_me_password_with_http_info(self, password_reset_body, **kwargs): ...
    async def put_me_password_async(self, password_reset_body, **kwargs): ...
    def put_users_id_password(self, user_id, password_reset_body, **kwargs): ...
    def put_users_id_password_with_http_info(self, user_id, password_reset_body, **kwargs): ...
    async def put_users_id_password_async(self, user_id, password_reset_body, **kwargs): ...
