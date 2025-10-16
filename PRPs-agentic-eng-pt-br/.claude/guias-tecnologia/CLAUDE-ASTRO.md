# CLAUDE.md

Este arquivo fornece orientação abrangente ao Claude Code ao trabalhar com aplicações Astro 5+ e a Arquitetura Islands.

## Filosofia Central de Desenvolvimento

### KISS (Keep It Simple, Stupid)

A simplicidade deve ser um objetivo-chave no design. Escolha soluções diretas sobre complexas sempre que possível. Soluções simples são mais fáceis de entender, manter e depurar.

### YAGNI (You Aren't Gonna Need It)

Evite construir funcionalidade por especulação. Implemente recursos apenas quando necessário, não quando você antecipa que podem ser úteis no futuro.

### Princípios de Design

- **Arquitetura Islands**: Envie JavaScript mínimo, hidrate apenas o que precisa de interatividade
- **Performance por Padrão**: Estático primeiro com hidratação seletiva para performance otimizada
- **Framework Agnóstico**: Misture React, Vue, Svelte e outros frameworks no mesmo projeto
- **Orientado a Conteúdo**: Otimizado para websites com muito conteúdo com gerenciamento de conteúdo type-safe
- **Zero JavaScript por Padrão**: Envie JavaScript apenas quando explicitamente necessário

## 🤖 Diretrizes para Assistente de IA

### Consciência de Contexto

- Ao implementar funcionalidades, sempre verifique padrões existentes primeiro
- Prefira geração estática sobre renderização client-side quando possível
- Use componentes específicos de framework apenas quando interatividade for necessária
- Verifique funcionalidades similares em diferentes integrações de framework
- Entenda quando usar `.astro` vs componentes de framework

### Armadilhas Comuns a Evitar

- Sobre-hidratar componentes que poderiam ser estáticos
- Misturar múltiplos frameworks desnecessariamente em componentes únicos
- Ignorar os benefícios de hidratação parcial do Astro
- Criar funcionalidade duplicada em diferentes islands de framework
- Sobrescrever integrações existentes sem verificar alternativas

### Padrões de Fluxo de Trabalho

- Preferencialmente criar testes ANTES da implementação (TDD)
- Use "pensar duro" para decisões de estratégia de hidratação
- Quebre componentes interativos complexos em islands menores e focados
- Valide escolha de framework e requisitos de hidratação antes da implementação

### Requisitos de Comandos de Pesquisa

**CRÍTICO**: Sempre use `rg` (ripgrep) em vez de comandos tradicionais `grep` e `find`:

```bash
# ❌ Não use grep
grep -r "pattern" .

# ✅ Use rg em vez disso
rg "pattern"

# ❌ Não use find com name
find . -name "*.ts"

# ✅ Use rg com filtragem de arquivo
rg --files | rg "\.ts$"
# ou
rg --files -g "*.ts"
```

**Regras de Aplicação:**

```
(
    r"^grep\b(?!.*\|)",
    "Use 'rg' (ripgrep) em vez de 'grep' para melhor performance e recursos",
),
(
    r"^find\s+\S+\s+-name\b",
    "Use 'rg --files | rg pattern' ou 'rg --files -g pattern' em vez de 'find -name' para melhor performance",
),
```

## 🧱 Estrutura de Código e Modularidade

### Limites de Arquivo e Componente

- **Nunca crie um arquivo com mais de 500 linhas de código.** Se aproximando deste limite, refatore dividindo em módulos ou componentes auxiliares.
- **Componentes Astro devem ter menos de 200 linhas** para melhor manutenibilidade.
- **Funções devem ser curtas e focadas, sub 50 linhas** e ter uma única responsabilidade.
- **Organize código por funcionalidade e framework**, mantendo componentes relacionados juntos.

## 🚀 Recursos-Chave do Astro 5+

### Content Layer (Novo no Astro 5)

- **Gerenciamento de Conteúdo Flexível**: Carregue conteúdo de qualquer fonte (arquivos, APIs, CMSs)
- **Conteúdo Type-Safe**: Tipos TypeScript automáticos para todas as coleções de conteúdo
- **Impulso de Performance**: Até 5x builds mais rápidos para Markdown, 2x para MDX
- **API Unificada**: Interface única para todas as fontes de conteúdo

```typescript
// content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string(),
  }),
});

const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    link: z.string().url(),
    github: z.string().url().optional(),
    image: z.string(),
    technologies: z.array(z.string()),
    featured: z.boolean().default(false),
  }),
});

export const collections = {
  blog,
  projects,
};
```

### Islands Architecture

```astro
---
// ✅ Componente Astro estático
import BlogPost from '../components/BlogPost.astro';
import CommentForm from '../components/CommentForm.tsx';
import LikeButton from '../components/LikeButton.svelte';

const { post } = Astro.props;
---

<html>
  <head>
    <title>{post.title}</title>
  </head>
  <body>
    <!-- Conteúdo estático - zero JavaScript -->
    <BlogPost post={post} />
    
    <!-- Island React - hidratação seletiva -->
    <CommentForm client:load postId={post.id} />
    
    <!-- Island Svelte - hidratação sob demanda -->
    <LikeButton client:idle postId={post.id} />
  </body>
</html>
```

### Diretivas de Hidratação

```astro
---
// ✅ Diferentes estratégias de hidratação
import InteractiveComponent from '../components/Interactive.tsx';
import LazyComponent from '../components/Lazy.tsx';
import CriticalComponent from '../components/Critical.tsx';
---

<!-- Hidratação imediata (crítico) -->
<CriticalComponent client:load />

<!-- Hidratação quando visível -->
<InteractiveComponent client:visible />

<!-- Hidratação quando ocioso -->
<LazyComponent client:idle />

<!-- Hidratação sob demanda -->
<LazyComponent client:media="(max-width: 768px)" />

<!-- Hidratação apenas em hover -->
<LazyComponent client:only="react" />
```

## 📁 Estrutura de Arquivos e Organização

### Estrutura do Projeto

```
src/
├── pages/
│   ├── index.astro
│   ├── about.astro
│   ├── blog/
│   │   ├── index.astro
│   │   └── [slug].astro
│   └── projects/
│       └── [slug].astro
├── components/
│   ├── astro/
│   │   ├── Layout.astro
│   │   ├── Header.astro
│   │   └── Footer.astro
│   ├── react/
│   │   ├── CommentForm.tsx
│   │   └── SearchBar.tsx
│   ├── vue/
│   │   ├── ImageGallery.vue
│   │   └── ContactForm.vue
│   └── svelte/
│       ├── Counter.svelte
│       └── LikeButton.svelte
├── content/
│   ├── config.ts
│   ├── blog/
│   │   ├── post-1.md
│   │   └── post-2.md
│   └── projects/
│       ├── project-1.md
│       └── project-2.md
├── layouts/
│   ├── BaseLayout.astro
│   ├── BlogLayout.astro
│   └── ProjectLayout.astro
├── styles/
│   └── global.css
└── utils/
    ├── date.ts
    └── slugify.ts
```

### Convenções de Nomenclatura

```typescript
// ✅ Arquivos Astro: PascalCase
// Layout.astro, Header.astro, BlogPost.astro

// ✅ Componentes React: PascalCase
// CommentForm.tsx, SearchBar.tsx

// ✅ Componentes Vue: PascalCase
// ImageGallery.vue, ContactForm.vue

// ✅ Componentes Svelte: PascalCase
// Counter.svelte, LikeButton.svelte

// ✅ Páginas: kebab-case
// about.astro, blog-post.astro

// ✅ Utilitários: camelCase
// dateUtils.ts, slugify.ts
```

## 🎯 Padrões de Componentes

### Componentes Astro

```astro
---
// ✅ Componente Astro bem estruturado
interface Props {
  title: string;
  description?: string;
  image?: string;
  date: Date;
  author: string;
  tags: string[];
}

const { title, description, image, date, author, tags } = Astro.props;

// Função utilitária
function formatDate(date: Date): string {
  return new Intl.DateTimeFormat('pt-BR').format(date);
}
---

<article class="blog-post">
  {image && (
    <img 
      src={image} 
      alt={title}
      class="hero-image"
      loading="lazy"
    />
  )}
  
  <header>
    <h1>{title}</h1>
    
    <div class="meta">
      <time datetime={date.toISOString()}>
        {formatDate(date)}
      </time>
      <span>por {author}</span>
    </div>
    
    {tags.length > 0 && (
      <div class="tags">
        {tags.map(tag => (
          <span class="tag">{tag}</span>
        ))}
      </div>
    )}
  </header>
  
  {description && (
    <p class="description">{description}</p>
  )}
  
  <slot />
</article>

<style>
  .blog-post {
    max-width: 800px;
    margin: 0 auto;
    padding: 2rem;
  }
  
  .hero-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 8px;
    margin-bottom: 2rem;
  }
  
  .meta {
    display: flex;
    gap: 1rem;
    margin: 1rem 0;
    color: #666;
    font-size: 0.9rem;
  }
  
  .tags {
    display: flex;
    gap: 0.5rem;
    flex-wrap: wrap;
  }
  
  .tag {
    background: #f0f0f0;
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8rem;
  }
</style>
```

### Componentes React (Islands)

```tsx
// ✅ Componente React para Astro
import { useState } from 'react';

interface CommentFormProps {
  postId: string;
}

export default function CommentForm({ postId }: CommentFormProps) {
  const [comment, setComment] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);
    
    try {
      await fetch('/api/comments', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ postId, comment }),
      });
      
      setComment('');
      // Mostrar sucesso
    } catch (error) {
      console.error('Erro ao enviar comentário:', error);
    } finally {
      setIsSubmitting(false);
    }
  };
  
  return (
    <form onSubmit={handleSubmit} className="comment-form">
      <textarea
        value={comment}
        onChange={(e) => setComment(e.target.value)}
        placeholder="Escreva seu comentário..."
        rows={4}
        required
      />
      
      <button 
        type="submit" 
        disabled={isSubmitting || !comment.trim()}
        className="submit-button"
      >
        {isSubmitting ? 'Enviando...' : 'Enviar Comentário'}
      </button>
    </form>
  );
}
```

### Componentes Vue (Islands)

```vue
<!-- ✅ Componente Vue para Astro -->
<template>
  <div class="image-gallery">
    <div class="gallery-grid">
      <div
        v-for="(image, index) in images"
        :key="index"
        class="gallery-item"
        @click="openModal(index)"
      >
        <img :src="image.thumbnail" :alt="image.alt" loading="lazy" />
      </div>
    </div>
    
    <div v-if="isModalOpen" class="modal" @click="closeModal">
      <div class="modal-content" @click.stop>
        <img :src="currentImage?.fullSize" :alt="currentImage?.alt" />
        <button class="close-button" @click="closeModal">&times;</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Image {
  thumbnail: string;
  fullSize: string;
  alt: string;
}

interface Props {
  images: Image[];
}

const props = defineProps<Props>();

const isModalOpen = ref(false);
const currentImageIndex = ref(0);

const currentImage = computed(() => 
  props.images[currentImageIndex.value]
);

function openModal(index: number) {
  currentImageIndex.value = index;
  isModalOpen.value = true;
}

function closeModal() {
  isModalOpen.value = false;
}
</script>

<style scoped>
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.gallery-item {
  cursor: pointer;
  overflow: hidden;
  border-radius: 8px;
}

.gallery-item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.gallery-item:hover img {
  transform: scale(1.05);
}

.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

.modal-content {
  position: relative;
  max-width: 90%;
  max-height: 90%;
}

.modal-content img {
  width: 100%;
  height: auto;
  border-radius: 8px;
}

.close-button {
  position: absolute;
  top: -40px;
  right: 0;
  background: none;
  border: none;
  color: white;
  font-size: 2rem;
  cursor: pointer;
}
</style>
```

## 🔗 Gerenciamento de Conteúdo

### Content Collections

```typescript
// content/config.ts
import { defineCollection, z } from 'astro:content';

const blog = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    pubDate: z.coerce.date(),
    updatedDate: z.coerce.date().optional(),
    heroImage: z.string().optional(),
    tags: z.array(z.string()).default([]),
    author: z.string(),
    featured: z.boolean().default(false),
  }),
});

const projects = defineCollection({
  schema: z.object({
    title: z.string(),
    description: z.string(),
    link: z.string().url(),
    github: z.string().url().optional(),
    image: z.string(),
    technologies: z.array(z.string()),
    featured: z.boolean().default(false),
    status: z.enum(['completed', 'in-progress', 'planned']).default('completed'),
  }),
});

export const collections = {
  blog,
  projects,
};
```

### Busca de Conteúdo

```astro
---
// ✅ Busca de conteúdo em página
import { getCollection } from 'astro:content';

// Buscar todos os posts do blog
const allPosts = await getCollection('blog');

// Filtrar posts em destaque
const featuredPosts = allPosts.filter(post => post.data.featured);

// Ordenar por data
const sortedPosts = allPosts.sort((a, b) => 
  b.data.pubDate.getTime() - a.data.pubDate.getTime()
);

// Buscar posts por tag
const reactPosts = allPosts.filter(post => 
  post.data.tags.includes('react')
);
---

<h1>Blog Posts</h1>

<div class="featured-posts">
  <h2>Posts em Destaque</h2>
  {featuredPosts.map(post => (
    <article>
      <h3>{post.data.title}</h3>
      <p>{post.data.description}</p>
      <a href={`/blog/${post.slug}`}>Ler mais</a>
    </article>
  ))}
</div>

<div class="all-posts">
  <h2>Todos os Posts</h2>
  {sortedPosts.map(post => (
    <article>
      <h3>{post.data.title}</h3>
      <p>{post.data.description}</p>
      <time>{post.data.pubDate.toLocaleDateString('pt-BR')}</time>
      <a href={`/blog/${post.slug}`}>Ler mais</a>
    </article>
  ))}
</div>
```

### Páginas Dinâmicas

```astro
---
// ✅ Página dinâmica para posts do blog
import { getCollection } from 'astro:content';
import BlogLayout from '../../layouts/BlogLayout.astro';

export async function getStaticPaths() {
  const posts = await getCollection('blog');
  
  return posts.map(post => ({
    params: { slug: post.slug },
    props: { post },
  }));
}

const { post } = Astro.props;
const { Content } = await post.render();
---

<BlogLayout title={post.data.title} description={post.data.description}>
  <article>
    <header>
      <h1>{post.data.title}</h1>
      <div class="meta">
        <time>{post.data.pubDate.toLocaleDateString('pt-BR')}</time>
        <span>por {post.data.author}</span>
      </div>
      
      {post.data.tags.map(tag => (
        <span class="tag">{tag}</span>
      ))}
    </header>
    
    <Content />
  </article>
</BlogLayout>
```

## 🎨 Estilização

### CSS Scoped

```astro
---
// ✅ Estilos scoped em componentes Astro
---

<div class="card">
  <h2>Card Title</h2>
  <p>Card content goes here.</p>
</div>

<style>
  .card {
    background: white;
    border-radius: 8px;
    padding: 1.5rem;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    margin: 1rem 0;
  }
  
  .card h2 {
    color: #333;
    margin-bottom: 1rem;
  }
  
  .card p {
    color: #666;
    line-height: 1.6;
  }
</style>
```

### Tailwind CSS

```astro
---
// ✅ Componente com Tailwind CSS
---

<div class="max-w-4xl mx-auto p-6">
  <div class="bg-white rounded-lg shadow-md p-6">
    <h1 class="text-3xl font-bold text-gray-900 mb-4">
      {title}
    </h1>
    
    <div class="flex items-center space-x-4 text-sm text-gray-600 mb-6">
      <time>{date.toLocaleDateString('pt-BR')}</time>
      <span>por {author}</span>
    </div>
    
    <div class="prose prose-lg max-w-none">
      <slot />
    </div>
  </div>
</div>
```

## 🧪 Testes

### Testes de Componente

```typescript
// ✅ Teste de componente Astro
import { describe, it, expect } from 'vitest';
import { render } from '@astrojs/test-utils';
import BlogPost from '../components/BlogPost.astro';

describe('BlogPost', () => {
  it('deve renderizar título e conteúdo', async () => {
    const props = {
      title: 'Teste Post',
      description: 'Descrição do teste',
      date: new Date('2024-01-01'),
      author: 'Autor Teste',
      tags: ['teste', 'astro'],
    };
    
    const { container } = await render(BlogPost, { props });
    
    expect(container.querySelector('h1')).toHaveTextContent('Teste Post');
    expect(container.querySelector('.description')).toHaveTextContent('Descrição do teste');
  });
});
```

### Testes de Página

```typescript
// ✅ Teste de página Astro
import { describe, it, expect } from 'vitest';
import { loadFixture } from '@astrojs/test-utils';
import { experimental_AstroContainer as AstroContainer } from '@astrojs/container';

describe('Blog Page', () => {
  it('deve renderizar lista de posts', async () => {
    const fixture = await loadFixture('./src/pages/blog/index.astro');
    const container = await AstroContainer.create(fixture);
    
    const result = await container.renderToString();
    
    expect(result).toContain('Blog Posts');
    expect(result).toContain('Todos os Posts');
  });
});
```

## 🔧 Configuração

### Astro Config

```typescript
// astro.config.mjs
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import vue from '@astrojs/vue';
import svelte from '@astrojs/svelte';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [
    react(),
    vue(),
    svelte(),
    tailwind(),
  ],
  output: 'static', // ou 'server' para SSR
  build: {
    assets: 'assets',
  },
  vite: {
    optimizeDeps: {
      include: ['react', 'react-dom'],
    },
  },
});
```

### TypeScript Config

```json
// tsconfig.json
{
  "extends": "astro/tsconfigs/strict",
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## 🚫 Anti-Padrões

### ❌ Evite

```astro
---
// ❌ Hidratação desnecessária
import StaticComponent from '../components/Static.tsx';
---

<!-- Não hidrate componentes estáticos -->
<StaticComponent client:load />
```

```astro
---
// ❌ Múltiplos frameworks desnecessários
import ReactComponent from '../components/React.tsx';
import VueComponent from '../components/Vue.vue';
---

<!-- Evite misturar frameworks sem necessidade -->
<ReactComponent client:load />
<VueComponent client:load />
```

### ✅ Faça

```astro
---
// ✅ Use componentes Astro para conteúdo estático
---

<!-- Conteúdo estático - zero JavaScript -->
<div class="static-content">
  <h1>Título</h1>
  <p>Conteúdo estático</p>
</div>

<!-- Hidrate apenas quando necessário -->
<InteractiveComponent client:visible />
```

## 📚 Recursos Adicionais

- [Documentação Astro](https://docs.astro.build/)
- [Content Collections](https://docs.astro.build/en/guides/content-collections/)
- [Islands Architecture](https://docs.astro.build/en/concepts/islands/)
- [Framework Integrations](https://docs.astro.build/en/guides/integrations-guide/)

---

**Lembre-se**: Foque em performance primeiro. Use componentes Astro para conteúdo estático e hidrate frameworks específicos apenas quando a interatividade for necessária. Aproveite a arquitetura Islands para otimizar o carregamento de JavaScript.
