from rest_framework.routers import DefaultRouter

from .views import ChallengeViewSet, LeaderboardEntryViewSet, SubmissionViewSet

router = DefaultRouter()
router.register("challenges", ChallengeViewSet, basename="challenge")
router.register("submissions", SubmissionViewSet, basename="submission")
router.register("leaderboard", LeaderboardEntryViewSet, basename="leaderboard")

urlpatterns = router.urls
