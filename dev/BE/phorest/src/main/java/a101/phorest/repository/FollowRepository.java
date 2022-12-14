package a101.phorest.repository;

import a101.phorest.domain.Follow;
import a101.phorest.domain.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface FollowRepository extends JpaRepository<Follow, Long> {

    @Query(nativeQuery = true, value = "select distinct * " +
            "from follow f " +
            "where f.follower_user_id = :userId")
    List<Follow> findAllByFollower(@Param("userId") Long userId);

    @Query(nativeQuery = true, value = "select distinct * " +
            "from follow f " +
            "where f.following_user_id = :userId")
    List<Follow> findAllByFollowing(@Param("userId") Long userId);

    @Query(nativeQuery = true, value = "select * " +
            "from follow f " +
            "where f.follower_user_id = :my_id " +
            "and f.following_user_id = :other_id")
    Optional<Follow> findByFollowerAndFollowing(@Param("other_id") Long other_id, @Param("my_id") Long my_id);

    Long countFollowByFollower(User follower);

    Long countFollowByFollowing(User following);

    @Modifying
    @Query(nativeQuery = true,value = "delete from follow where follower_user_id =:userId")
    void deleteAllByFollowerUserId(@Param("userId") Long userId);

    @Modifying
    @Query(nativeQuery = true,value = "delete from follow where following_user_id =:userId")
    void deleteAllByFollowingUserId(@Param("userId") Long userId);
}
