package br.com.etechoracio.study.service;

import br.com.etechoracio.study.entity.Disciplina;
import br.com.etechoracio.study.repository.DisciplinaRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class DisciplinaService {
    @Autowired
    private DisciplinaRepository repository;

    public Disciplina cadastrarDisciplina(Disciplina disciplina){
        var existe = repository.findByNomeIgnoreCase(disciplina.getNome());
        if(existe.isEmpty())
            return repository.save(disciplina);
        else
            throw new RuntimeException("Nome da disciplina já cadastrada");
    }

    public List<Disciplina> listar(){
        return repository.findAll();
    }

    public Optional<Disciplina> buscarPorId(Long id){
        var disciplina = repository.findById(id);
        return disciplina;
    }

    public Disciplina atualizar(Disciplina disciplina){
        return repository.save(disciplina);
    }

    public void excluir(Disciplina disciplina){ //(Long id)
        repository.deleteById(disciplina.getId());
    }


}
