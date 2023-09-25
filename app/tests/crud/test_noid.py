# from uuid_extensions import uuid7
# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi import HTTPException
# from app.crud.minter import create_minter
# from app.models.minter import MinterCreate
# from models.noid import MintRequest, NoidCreate
# from crud.noid import get_noid, get_noid_by_binding, mint_noids
# from noid import mint as mint_noid


# async def test_mint_noids(session: AsyncSession):
#     minter = MinterCreate(naa="naa", template="template", scheme="scheme")
#     created_minter = await create_minter(session, minter)

#     noid = NoidCreate(
#         noid=mint_noid(
#             n=minter.last_n,
#             template=minter.template,
#             scheme=minter.scheme,
#             naa=minter.naa,
#         ),
#         binding="test"
#     )

#     created_noid = await mint_noids(session, db_minter=created_minter, mint=MintRequest(bindings="test"))
#     await len(created_noid.noids) == 1
#     assert created_noid.noids[0].binding == noid.binding
#     assert created_noid.noids[0].noid == noid.noid
#     assert created_noid.noids[0].created_at is not None
#     assert created_noid.noids[0].updated_at is not None


# # def test_get_noid():
# #     n = 0
# #     assert mint_new_noid(n=n) == '00000000'
# #     n = n+1
# #     assert mint_new_noid(n=n) == '00000017'

# # def test_get_noid_with_naa():
# #     n = 0
# #     assert mint_new_noid(n=n, naa='id') == 'id/00000000'
# #     n = n+1
# #     assert mint_new_noid(n=n, naa='id') == 'id/00000017'

# # async def test_create_duplicate_iri(session: AsyncSession):
# #     iri = IRICreate(key="123456")
# #     await create_iri(session, iri)
# #     try:
# #         await create_iri(session, iri)
# #     except HTTPException as e:
# #         assert e.status_code == 409
# #         assert e.detail == "iri already exists"


# # async def test_get_iri(session: AsyncSession):
# #     iri = IRICreate(key="123456")
# #     created_iri = await create_iri(session, iri)
# #     retrieved_iri = await get_iri(session, created_iri.id)
# #     assert retrieved_iri == created_iri


# # async def test_get_nonexistent_iri(session: AsyncSession):
# #     retrieved_iri = await get_iri(session, uuid7())
# #     assert retrieved_iri is None


# # async def test_get_iri_by_key(session: AsyncSession):
# #     iri = IRICreate(key="123456")
# #     created_iri = await create_iri(session, iri)
# #     retrieved_iri = await get_iri_by_key(session, iri.key)
# #     assert retrieved_iri == created_iri


# # async def test_get_nonexistent_iri_by_key(session: AsyncSession):
# #     retrieved_iri = await get_iri_by_key(session, "123456")
# #     assert retrieved_iri is None


# # async def test_update_iri(session: AsyncSession):
# #     created_iri = await create_iri(
# #         session, IRICreate(namespace="http://example.org/", key="123456")
# #     )
# #     updated_iri = await update_iri(
# #         session, created_iri.id, IRIUpdate(namespace="http://example.org/")
# #     )
# #     assert updated_iri.id == created_iri.id
# #     assert updated_iri.key == "123456"
# #     assert updated_iri.namespace == "http://example.org/"


# # async def test_update_nonexistent_iri(session: AsyncSession):
# #     try:
# #         await update_iri(session, uuid7(), IRIUpdate(namespace="http://example.org/"))
# #     except HTTPException as e:
# #         assert e.status_code == 404
# #         assert e.detail == "iri not found"


# # async def test_delete_iri(session: AsyncSession):
# #     created_iri = await create_iri(session, IRICreate(key="123456"))
# #     deleted_count = await delete_iri(session, created_iri.id)
# #     assert deleted_count == 1
# #     retrieved_iri = await get_iri(session, created_iri.id)
# #     assert retrieved_iri is None


# # async def test_delete_nonexistent_iri(session: AsyncSession):
# #     deleted_count = await delete_iri(session, uuid7())
# #     assert deleted_count == 0
