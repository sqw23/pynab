"""Add a tonne of indexes, because postgres doesn't automatically create referencing FK indexes.

Revision ID: 53928162b90
Revises: None
Create Date: 2014-05-10 10:57:48.380065

"""

# revision identifiers, used by Alembic.
revision = '53928162b90'
down_revision = None

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_binaries_regex_id'), 'binaries', ['regex_id'], unique=False)
    op.create_index(op.f('ix_categories_parent_id'), 'categories', ['parent_id'], unique=False)
    op.create_index(op.f('ix_episodes_tvshow_id'), 'episodes', ['tvshow_id'], unique=False)
    op.create_index(op.f('ix_files_release_id'), 'files', ['release_id'], unique=False)
    op.create_index(op.f('ix_groups_active'), 'groups', ['active'], unique=False)
    op.create_index(op.f('ix_movies_name'), 'movies', ['name'], unique=False)
    op.create_index(op.f('ix_parts_binary_id'), 'parts', ['binary_id'], unique=False)
    op.create_index(op.f('ix_parts_group_name'), 'parts', ['group_name'], unique=False)
    op.create_index(op.f('ix_parts_posted'), 'parts', ['posted'], unique=False)
    op.create_index(op.f('ix_parts_total_segments'), 'parts', ['total_segments'], unique=False)
    op.drop_index('ix_parts_subject', table_name='parts')
    op.create_index(op.f('ix_releases_category_id'), 'releases', ['category_id'], unique=False)
    op.create_index(op.f('ix_releases_episode_id'), 'releases', ['episode_id'], unique=False)
    op.create_index(op.f('ix_releases_group_id'), 'releases', ['group_id'], unique=False)
    op.create_index(op.f('ix_releases_movie_id'), 'releases', ['movie_id'], unique=False)
    op.create_index(op.f('ix_releases_movie_metablack_id'), 'releases', ['movie_metablack_id'], unique=False)
    op.create_index(op.f('ix_releases_nfo_id'), 'releases', ['nfo_id'], unique=False)
    op.create_index(op.f('ix_releases_nfo_metablack_id'), 'releases', ['nfo_metablack_id'], unique=False)
    op.create_index(op.f('ix_releases_nzb_id'), 'releases', ['nzb_id'], unique=False)
    op.create_index(op.f('ix_releases_rar_metablack_id'), 'releases', ['rar_metablack_id'], unique=False)
    op.create_index(op.f('ix_releases_regex_id'), 'releases', ['regex_id'], unique=False)
    op.create_index(op.f('ix_releases_search_name'), 'releases', ['search_name'], unique=False)
    op.create_index(op.f('ix_releases_tvshow_id'), 'releases', ['tvshow_id'], unique=False)
    op.create_index(op.f('ix_releases_tvshow_metablack_id'), 'releases', ['tvshow_metablack_id'], unique=False)
    op.create_index(op.f('ix_releases_unwanted'), 'releases', ['unwanted'], unique=False)
    op.create_index(op.f('ix_segments_part_id'), 'segments', ['part_id'], unique=False)
    op.create_index(op.f('ix_segments_segment'), 'segments', ['segment'], unique=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_segments_segment'), table_name='segments')
    op.drop_index(op.f('ix_segments_part_id'), table_name='segments')
    op.drop_index(op.f('ix_releases_unwanted'), table_name='releases')
    op.drop_index(op.f('ix_releases_tvshow_metablack_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_tvshow_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_search_name'), table_name='releases')
    op.drop_index(op.f('ix_releases_regex_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_rar_metablack_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_nzb_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_nfo_metablack_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_nfo_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_movie_metablack_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_movie_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_group_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_episode_id'), table_name='releases')
    op.drop_index(op.f('ix_releases_category_id'), table_name='releases')
    op.create_index('ix_parts_subject', 'parts', ['subject'], unique=False)
    op.drop_index(op.f('ix_parts_total_segments'), table_name='parts')
    op.drop_index(op.f('ix_parts_posted'), table_name='parts')
    op.drop_index(op.f('ix_parts_group_name'), table_name='parts')
    op.drop_index(op.f('ix_parts_binary_id'), table_name='parts')
    op.drop_index(op.f('ix_movies_name'), table_name='movies')
    op.drop_index(op.f('ix_groups_active'), table_name='groups')
    op.drop_index(op.f('ix_files_release_id'), table_name='files')
    op.drop_index(op.f('ix_episodes_tvshow_id'), table_name='episodes')
    op.drop_index(op.f('ix_categories_parent_id'), table_name='categories')
    op.drop_index(op.f('ix_binaries_regex_id'), table_name='binaries')
    ### end Alembic commands ###
