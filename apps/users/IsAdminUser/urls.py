path('users/<int:user_id>/active/', UserToggleActiveView.as_view(), name='user-toggle-active'),