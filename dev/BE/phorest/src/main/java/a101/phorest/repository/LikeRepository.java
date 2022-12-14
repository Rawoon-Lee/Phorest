package a101.phorest.repository;

import a101.phorest.domain.Like;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface LikeRepository extends JpaRepository<Like, Long> {
    @Query(nativeQuery = true, value ="select distinct * " +
            "from postlike pl join user r on pl.user_id = r.user_id " +
            "where pl.post_id = :postId " +
            "and r.username = :username")
    Optional<Like> findByPostIdAndUsername(@Param("postId") Long postId, @Param("username") String username);


    @Query(nativeQuery = true, value = "select * from postlike where user_id =:userId")
    List<Like> findAllByUserId(@Param("userId") Long userId);

    @Modifying(clearAutomatically = true)
    @Query(nativeQuery = true, value = "delete from postlike where user_id =:userId")
    void deleteAllByUserId(@Param("userId")Long userId);

    @Modifying(clearAutomatically = true)
    @Query(nativeQuery = true, value = "delete from postlike where post_id =:postId")
    void deleteAllByPostId(@Param("postId") Long postId);



}
