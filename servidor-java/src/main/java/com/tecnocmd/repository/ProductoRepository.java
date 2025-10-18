// ProductoRepository.java

package com.tecnocmd.repository;

import com.tecnocmd.model.Producto;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface ProductoRepository extends JpaRepository<Producto, Integer> {
    List<Producto> findByMarcaIgnoreCase(String marca);
}